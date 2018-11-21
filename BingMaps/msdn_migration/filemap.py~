'''

When submitting a pull request to update content, MS Docs OBS generates a build report, as a CVS file, containing data for all the broken links in the repo.

This Python module reads in that build report, along with a YAML file for the MSDN/old link/new link data for each Bing Maps .md file, and then fixes the broken links in the repo.

'''

from pathlib import Path


class FileMap:

    def __init__(self, parent=Path('.'), ignore_dir=[]):

        files = []
        self.children = []
        self.path = parent
            
        for p in self.path.iterdir():
            if p.is_dir() and p.name not in ignore_dir:
                new_map = FileMap(p)
                self.children.append(new_map)
        for f in self.path.glob('*.md'):
            files.append(f)

        self.files = frozenset(files)

    @property
    def file_names(self):
        return [f.name for f in self.files]
        
    def get_path(self, *path_names):
        '''Returns a `Path` object from a list of folder/file names.
           It is expected that the last string ends with the '.md' extention.
        '''
        # print(f'paths: {path_names}')
        
        if not path_names:
            raise IndexError("Can't get path from empty path")

        head = path_names[0]
        tail = path_names[1:]

        # print(f'split: {head}-{tail}')

        if head in self.file_names:
            for f in self.files:
                if f.name == head:
                    return f
            raise IndexError('False positive: file not found')
        for kid in self.children:
            if kid.path.name == head:
                ret = kid.get_path(*tail)
                if ret:
                    return ret
        return None
            

    def create_link(self, source_path, dest_path):
        from os.path import relpath
        
        assert(issubclass(type(source_path), Path)), f'Source path expected type `Path` but got {type(source_path)}'
        assert(issubclass(type(dest_path), Path)), f'Dest path expected type `Path` but got {type(dest_path)}'

        return relpath(dest_path, start=source_path)
        
    def print(self, n=0):

        tab = '\t' * n

        print(f'{tab}name: "{self.path.name}"')
        print(f'{tab}files: {",".join(self.file_names)}')
        for kid in self.children:
            kid.print(n+1)


if __name__=="__main__":
    tmp = FileMap()
    # tmp.print()

    test_link_1 = ['rest-services', 'elevations', 'index.md']
    test_link_2 = ['v8-web-control', 'map-control-api', 'index.md']

    a = tmp.get_path(*test_link_1)
    b = tmp.get_path(*test_link_2)
    print(a, b)
    p = tmp.create_link(a, b)
    print(p)

        
        
        
        
