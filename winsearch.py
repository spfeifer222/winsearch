import re

from wcmatch.pathlib import Path


class Place:

    G = [Path(r'G:\Abteilung-3\32\Pfeifer')]
    I =  [Path(r'i:')]
    C = [Path('c:\\')]
    C_USER = [Path(r'C:\Users\pfeifer')]
    C_PROGR =  [Path(r'C:\Program Files (x86)')]
    C_USER_PROGR = [Path(r'C:\Users\pfeifer'), 
                    Path(r'C:\Program Files (x86)')]
    ALL = [Path(r'G:\Abteilung-3\32\Pfeifer'),
           Path(r'i:'),
           Path(r'C:\Users\pfeifer'),
           Path(r'C:\Program Files (x86)')]


class WinSearch:

    def glob_search(self, *globs, places, **kwargs):
        """Returns a glob search result on given places.

        Args:
            globs (str): glob search sting(s)
            places (Place class attribute): Path descriptions defined in Place class attributes
        """
        print(f"Running glob search on {globs} in {places}...\n")

        for place in places:
            #print(f"{lw}: {'exists' if lw.exists() else 'does not exist'}")
            for file in place.rglob(globs):
                print(file)
        
    def regex_search(self, *regex, places, **kwargs):
        """Returns a regex search result on given places.

        Args:
            regex (str): regex expression(s)
            places (Place class attribute): Path descriptions defined in Place class attributes

        Note: regex expressions could be raw strings to escape special characters
        """
        print(f"Running regex search on {regex} in {places}...\n")

        for place in places:
            #print(f"{lw}: {'exists' if lw.exists() else 'does not exist'}")
            for file in place.rglob('*'):
                for reg in regex:
                    if re.search(reg, str(file)):
                        print(file)

if __name__ == '__main__':

    winsearch = WinSearch()
    #winsearch.glob_search('settings.json', places=Place.C)
    winsearch.glob_search('Microsoft.PowerShell_profil*', places=Place.C)
    #winsearch.regex_search('settings.json$', places=Place.C)