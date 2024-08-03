import src
import os
import json
from config import config


data_object = {
    'source' : {
        'raw' : "",
        'edit' : {}
    },
    'destination' : {
        'raw' : "",
        'edit' : {}
    }
}


class Crawl:
    def __init__(self, data):
        self.data = data


# App enters here

def main():
    crawl = Crawl("None")
    selection = None
    while selection == None:
        # User input selection
        selections = ['Settings', 'Crawl', 'Quit']
        options = ""
        for option in selections:
            options = options + f"{int(selections.index(option))+1}) {option} "
        print(f'Crawl data: {crawl.data}')
        print(options)
        raw_selection = input("Please choose a option number:")
        selection = selections[int(raw_selection)-1].lower()

        if selection == 'settings':
            build_dirs()
            selection = None

            continue

        elif selection == 'crawl':
            crawl.data = find()
            selection = None

            continue

        elif selection == 'quit':
            print("Goodbye")
            exit()

            
'''
Settings branch
Build directory tree
Store Library location
Store favorites locations
'''

def build_dirs():
    raw = input("Absolute path or type 'back': ")
    if raw == 'back':
        return
    else:
        build_path = raw +"/"+"Rom Library"

    print(build_path)
    try:
        os.makedirs(build_path)
    except OSError:
        print('Library already built')
        built = True

    if not built:
        for key in config.rom_groups.keys():
            print(key)
            try:
                os.makedirs(build_path+'/'+str(key))
            except OSError:
                pass
    
    return

'''
Main crawl functions
Find by ext
Find by named dir
'''
    
def find():
    '''Returns dictionary of lists.'''
    dir = None
    favorites = ["/media/xreddr/7C9C-465F", "/media/xreddr/Lexar/EmuPulls"]
    for i in range(len(favorites)):
        print(i, end=' )')
        print(favorites[i])
    select_fav = input('Select favorite?')
    if select_fav == '':
        pass
    elif favorites[int(select_fav)]:
        dir = favorites[int(select_fav)]
    
    ext = None
    while dir == None:
        dir = input("Input absolute path:")
    while ext == None:
        ext = input("input extension:")

    s1 = src.search.Scanner(dir, ext)
    s1.search()
    print(json.dumps(s1.found, indent=2))

    return s1.found

def rename(found):
    print('Select options:\n1) Remove numbering\n2) Remove bracketing\n3) Remove both')
    raw = input()
    valid = raw.lower()
    if valid == '1':
        src.search.remove_numbering(found)
        print('Numbering removed from file names.')
    elif valid == '2':
        print("In development")
    elif valid == '3':
        print("In development")

    return

if __name__ == '__main__':
    main()