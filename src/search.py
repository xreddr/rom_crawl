import os, json, shutil
import jfs

def debug():
    dir = '/media/xreddr/Lexar/EmuPulls/SNES'
    # dir = '/media/xreddr/7C9C-465F'
    ext = None
    while dir == None:
        dir = input("Input absolute path:")
    while ext == None:
        ext = input("input extension:")

    s1 = Scanner(dir, ext)
    s1.search()
    if s1.found:
        remove_brackets(s1.found)
    else:
        print('Nothing found.')


class Scanner:
    def __init__(self, dir, ext):
        self.dir = dir
        self.ext = ext

    def search(self):
        '''Defines self.found as dictionary of lists'''
        found = {}
        for root, dirs, files in os.walk(self.dir):
            for file in files:
                if file.endswith(self.ext):
                    key = os.path.dirname(os.path.join(root, file))
                    if key not in found:
                        found.update({key:[]})
                    found[key].append(file)
        self.found = found


def remove_numbering(found):
    '''Takes dict of lists'''
    for dir in found:
        for file in found[dir]:
            exlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '.']
            newname = file
            while newname[0] in exlist:
                newname = newname[1:]
            old_file = os.path.join(dir, file)
            new_file = os.path.join(dir, newname)
            if os.path.exists(old_file) and new_file != old_file:
                os.rename(old_file, new_file)
                if os.path.exists(new_file):
                    print(f'{old_file} has been renamed to {new_file}')

def remove_brackets(found):
    rev = {}
    for dir in found:
        rev.update({dir : found[dir]})
        for file in found[dir]:
            print(file)
            newname = jfs.remove_text_inside_brackets(file)
            print(newname)
            rev[dir] = [sub.replace(f'{file}', f'{newname}') for sub in rev[dir]]
    print(json.dumps(found, indent=2))
    print(json.dumps(rev, indent=2))
    return rev

def copy_file(found, target):
    for dir in found:
        for file in found[dir]:
            exlist = ['(U)']
            src = os.path.join(dir, file)
            dst = os.path.join(target, file)
            shutil.copyfile(src, dst)

if __name__ == "__main__":
    debug()