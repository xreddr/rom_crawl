import src

def main():
    crawl = None
    selection = None
    while selection == None:

        selection = welcome()

        if selection == 'find':
            crawl = find()
            selection = None

            continue

        if selection == 'name':
            if crawl:
                rename(crawl)
            else:
                print('No found selection')
            selection = None
            
            continue
            

def welcome():
    '''Returns string.'''
    selection = None
    while selection == None:
        print("Welcome to Rom Crawl\n1) Find\n2) Rename\n3) Copy\n4) Organize\n5) Manage")
        raw = input("Please select an option: ")
        valid = raw.lower()
        if valid == '1':
            selection = 'find'
        elif valid == '2':
            selection = 'name'
        elif valid == '3':
            selection = 'copy'
        elif valid == '4':
            selection = 'org'
        elif valid == '5':
            selection = 'mng'

        return selection
    
def find():
    '''Returns dictionary of lists.'''
    dir = None
    ext = None
    while dir == None:
        dir = input("Input absolute path:")
    while ext == None:
        ext = input("input extension:")

    s1 = src.search.Scanner(dir, ext)
    s1.search()

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