import os, json, shutil

directory = "/media/xreddr/Lexar/mac_archive/photos/Photography"
target = "/home/xreddr/Documents/test/storage"

class Scanner:
    def __init__(self, dir):
        self.dir = dir

    def search(self):
        '''Defines self.found as dictionary of lists'''
        found = {}
        limit = 3
        for root, dirs, files in os.walk(self.dir):
            for dir in dirs:
                key = os.path.dirname(os.path.join(root, dir))
                if key not in found:
                    found.update({key:[]})
                found[key].append(dir)
            break
        for i in found:
            for k in found[i]:
                print(k)
        self.found = found
    
def main():
    directory = "/media/xreddr/Lexar/mac_archive/photos/Photography"
    target = "/home/xreddr/Documents/test/storage"
    s1 = Scanner(directory)
    s1.search()
    print(json.dumps(s1.found, indent=2))
          

if __name__ == "__main__":
    main()