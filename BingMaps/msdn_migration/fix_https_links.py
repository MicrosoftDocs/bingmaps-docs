from filemap import FileMap
from pandas import read_excel
from os.path import expanduser as ospath

# data_file = 'msdn_migration/bad_http_links.csv'

data_file = 'msdn_migration/bad_external_links.csv'

mapper = FileMap(ignore_dir=['msdn_migration'])


def get_http_data():
    with open(data_file, 'r', encoding='utf-8') as f:
        for n, line in enumerate(f.readlines()):
            if n > 0:
                row = line.split(',')
                yield row

def get_excel_data():
    with open(data_file, 'r', encoding='utf-8') as f:
        lines = list(f.readlines())
        n = len(lines)
        for i in range(1, n, 3):
            rows = lines[i].split(',')
            print(rows)
            source = rows[1]
            link = rows[6].split('URL: ""')[1].split('""')[0]
            yield source, link
            # i += 2

broken_url_head = 'The following referenced link ['
broken_url_tail = '] supports HTTPS. Please change the link to use HTTPS.\n'

def get_url(array):
    for a in array:
        if 'URL' in a:
            return a.split('URL: ""')[1].split('""')[0]
    return None

d = {}

lines = list(get_http_data())
n = len(lines)

for i in range(0, n, 3):
    if len(lines[i]) > 1:
        sources = lines[i][1]
        d[sources] = get_url(lines[i+2])
        # d[sources] = lines[i+2][0].split('URL: ""')[1].split('""')[0]
from pprint import pprint
pprint(d)
    
    




'''
N = len(broken_url_head)
M = len(broken_url_tail)
    
for source, link in get_excel_data():

    strip_head = 'https://github.com/MicrosoftDocs/bingmaps-docs/blob/master/BingMaps/'
    head_len = len(strip_head)

    # test_url_raw = row[-1]

    # test_url_raw = row[5]
    # print(test_url_raw)
    # exit(1)
    
    source_file_parts = source[head_len:].split('/')

    path = mapper.get_path(*source_file_parts)

    if path:
        html = None
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()

        if html:
            non_sec = 'http://'
            sec = 'https://'

            if sec in new_link:
                _out = sec
                _in = new_sec
            else:
                _out = new_sec
                _in = sec
            
            
            new_link = link.replace(_out, _in)
            new_html = html.replace(link, new_link)
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_html)

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


                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_html)
                    print(f'replaced: {path}')
        else:
            print(f'\nError:\n\t{source_file_parts}\n')
'''
