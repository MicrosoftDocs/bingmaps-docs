from filemap import FileMap

from os.path import expanduser as ospath

data_file = 'msdn_migration/bad_http_links.csv'

mapper = FileMap(ignore_dir=['msdn_migration'])


def get_http_data():
    with open(data_file, 'r', encoding='utf-8') as f:
        for n, line in enumerate(f.readlines()):
            if n > 0:
                yield line.split(',')
            

broken_url_head = 'The following referenced link ['
broken_url_tail = '] supports HTTPS. Please change the link to use HTTPS.\n'

N = len(broken_url_head)
M = len(broken_url_tail)
    
for row in get_http_data():

    # exit(1)
    strip_head = 'https://github.com/MicrosoftDocs/bingmaps-docs/blob/master/BingMaps/'
    head_len = len(strip_head)

    test_url_raw = row[-1]
    

    if broken_url_head in test_url_raw:
        source_file_parts = row[1][head_len:].split('/')
        length = len(test_url_raw)
        link = test_url_raw[N+1: length - M]

        path = mapper.get_path(*source_file_parts)

        if path:
            html = None
            with open(path, 'r', encoding='utf-8') as f:
                html = f.read()


            if html:
                new_link = link.replace('http://', 'https://')
                new_html = html.replace(link, new_link)
                print(f'link:\n\t{link}\nnew link:\n\t{new_link}')
                if html != new_html:

                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_html)
                        print(f'replaced: {path}')
        else:
            print(f'\nError:\n\t{source_file_parts}\n')
