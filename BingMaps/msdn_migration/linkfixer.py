from pandas import read_csv
import sys
import yaml
from collections import namedtuple, defaultdict

BuildData = namedtuple('BuildData', 'source_file_parts dest_file_parts old_dest_link new_filename') 


def check_extension(file_name, ext):
    return file_name.split('.')[-1] == ext

def parse_msg(msg):
    '''Parse data from OBS report'''
    if 'Invalid file link' in msg:
        bad_link = msg.split(':(')[1].split(').')[0]
        bad_link_parts = bad_link.split('/')
        bad_link_parts.remove('~')
        return bad_link.replace('~', '..'), bad_link_parts
    return None

def get_updated_parts(link_data, source_link_parts):
    service = source_link_parts[0]
    old_md_file = source_link_parts[-1]
    for serv in link_data:
        if serv.get('path') == service:
            for link_dict in serv.get('links'):
                if link_dict['old-docs'] == old_md_file:
                    return [service] + link_dict['new-docs'].split('/')
    return old_md_file

def get_error_data(df, link_data):
    '''
    Prepares doc data from OBS report and YAML link mapper file
    into `ErrorData` objects to be used to replace links in repo

    - `df` is a Pandas dataframe of OBS linking error info
    - `link_data` is a dict from the YAML link data file
    '''

    for [f, msg] in df[['File','Message']].values:
        # print(f'\nunparsing: "{f} -- {msg}"\n')
        parse_data = parse_msg(msg)
        if parse_data and check_extension(f, 'md'):

            old_dest_link, dest_path_parts = parse_data
            
            if '.md' in dest_path_parts[-1]:

                # get dest file
                new_dest_path_parts = get_updated_parts(link_data, dest_path_parts)
                new_filename = new_dest_path_parts[-1]
                source_path_parts = f.split('/')
                source_path_parts.remove('BingMaps')
                datum = BuildData(source_path_parts, new_dest_path_parts, old_dest_link, new_filename)
                yield datum


def replace_link(file_str, old_link, link):
    '''Problem: OBS replaces '../../../' etc. with '~'
    '''
    new_file_str = file_str
    try:
        index = file_str.index(old_link)
        n = len(old_link)

        if index > -1:
            top = file_str[:index]
            bot = file_str[index+n:]
            while any(top):
                if top[-1] != '(':
                    top.pop()
                else:
                    break
            new_file_str = top + link + bot
            new_file_str = replace_link(new_file_str, old_link, link)
    except ValueError:
        pass
    finally:
        return new_file_str

def update_file(mapper, datum, link):
    try:
        file_str = None
        source_file_path = mapper.get_path(*datum.source_file_parts, full=True)
        print(f'source file change: "{source_file_path}"\n')

        print('opening file')
        with open(source_file_path, 'r', encoding='utf-8') as f:
            file_str = f.read()

        file_old = file_str
        # file_str = file_str.replace(datum.old_dest_link, link)
        file_str = replace_link(file_str, datum.old_dest_link, link)

        if file_str != None and file_str != file_old:
            print('replacing file')
            with open(source_file_path, 'w', encoding='utf-8') as f:
                print(f'Input data: {datum}', f'link: {link}')
                f.write(file_str)
                print(f'Changed file!')
        else:
            print('Bad datum:\n', datum)

    except UnicodeDecodeError as e:
        print(f'Failed to open {source_file_path}: \n {e}')
        exit(1)
            
                
def update_links(obs_cvs_file, yaml_data_file):

    yaml_links = None
    with open(yaml_data_file, 'r') as f:
        yaml_links = yaml.load(f)

    df = read_csv(obs_cvs_file, sep=',')

    from filemap import FileMap

    ignore = [] # ['v8-web-control']
    
    mapper = FileMap(ignore_dir=ignore)
        
    for data in get_error_data(df, yaml_links):
       
        new_dest = list(data.dest_file_parts)
        new_dest[-1] = data.new_filename

        source = mapper.get_path(*data.source_file_parts)
        dest = mapper.get_path(*new_dest)
       
        link = mapper.create_link(source, dest)

        if link:
            if link == '.':
                link = data.new_filename
            print(f'Data: {data}')
            print(f'Link: "{link}"\n')
            update_file(mapper, data, link)
            
if __name__=='__main__':
    print('\nLoading link fixer, usage:\n\n\t$> link_fixer {csv_report_file} {yaml_link_file}\n')
    yaml_file = None
    cvs_file = None
    if len(sys.argv) > 2:
        cvs_file = sys.argv[1]
        yaml_file = sys.argv[2]
        update_links(cvs_file, yaml_file)        
    else:
        exit(1)

    


            
