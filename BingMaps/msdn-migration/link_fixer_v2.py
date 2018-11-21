'''

When submitting a pull request to update content, MS Docs OBS generates a build report, as a CVS file, containing data for all the broken links in the repo.

This Python module reads in that build report, along with a YAML file for the MSDN/old link/new link data for each Bing Maps .md file, and then fixes the broken links in the repo.

'''

from pathlib import Path


class FileMap(Path):

    def __init__(self, parent=Path('.'), ignore_dir=[]):

        self.files = []
        self.children = []
        
        super(list, self).__init__(parent)
            
        for p in self.iterdir():
            if p.is_dir() and p.name not in ignore_dir:
                new_map = FileMap(parent=p)
                self.children.append(p)
            elif p.name.split('.')[-1] is 'md':
                self.files.append(p.name)
                    

        
        
        
        
