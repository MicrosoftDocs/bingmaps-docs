from pandas import read_csv
import sys
import yaml
from collections import namedtuple, defaultdict
import re
from pathlib import Path

ErrorData = namedtuple('ErrorData', 'dest_file service_dir md_file old_link new_link') 

def parse_msg(msg):
    '''Parse data from OBS report'''
    objs = re.match(r'Invalid file link:\(\~\/([-\w]+)\/([-\w]+\/)([-\w]+)\.md\).', msg)
    if objs:
        return objs.group(1), f'{objs.group(3)}.md'
    return None

def check_extension(file_name, ext):
    return file_name.split('.')[-1] == ext

# def get_link_data():
    
    
def get_error_data(df, link_data):
    '''
    Prepares doc data from OBS report and YAML link mapper file
    into `ErrorData` objects to be used to replace links in repo
    '''
    for [file, msg] in df[['File','Message']].values:
        print(f'unparsing: "{file} -- {msg}"\n')
        parse_data = parse_msg(msg)
        if parse_data and check_extension(file, 'md'):
            service_dir, md_file  = parse_data
            old_link = f'../{service_dir}/{md_file}'           
            dest_file = file.replace('BingMaps', '..')
            for service in link_data:
                if service.get('path') == service_dir:
                    for link_dict in service.get('links'):
                        if link_dict['old-docs'] == md_file:
                            new_link_file = link_dict.get('new-docs')
                            if new_link_file:
                                new_link = f'BingMaps/{service_dir}/{new_link_file}'
                                yield ErrorData(dest_file, service_dir, md_file, old_link, new_link)
                                continue


def update_file(error_object):
    file_name = str(Path(error_object.dest_file).absolute())
    file_str = None
    with open(file_name, 'r', encoding='utf8') as f:
        file_str = f.read()
    file_old = file_str
    file_str = file_str.replace(error_object.old_link, error_object.new_link)
    if file_str != None and file_str != file_old:
        with open(file_name, 'w', encoding='utf8') as f:
            f.write(file_str)
            print(f'Changed file "{error_object.dest_file}": "{error_object.old_link}" --> "{error_object.new_link}"')


'''
def relink_repo(error_data):
    for datum in error_data:
        # get write access to file to change
        file_as_string = None
        with open(get_dest_file_path(data.dist_file), 'w') as dest_f:
            file_as_string = dest_f.read()
            file_as_string.replace(
'''     


if __name__=='__main__':
    print('\nLoading link fixer, usage:\n\n\t$> link_fixer {csv_report_file} {yaml_link_file}\n')
    
    yaml_links = None
    excel_filename = None
    if len(sys.argv) > 2:
        excel_filename = sys.argv[1]
        with open(sys.argv[2], 'r') as f:
            yaml_links = yaml.load(f)
    else:
        exit(1)
        
    df = None
    if excel_filename:
        df = read_csv(excel_filename, sep=',')

    for err_fix in get_error_data(df, yaml_links):
        print(f'\t ---> {err_fix}\n')
        update_file(err_fix)
    
