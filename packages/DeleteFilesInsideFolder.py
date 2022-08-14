import os
def DeleteInsideFolder(folderpath):

        # folder path
    dir_path = folderpath
    count = 0
        # Iterate directory
    for path in os.listdir(dir_path):
            # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    print('\n           Number of Files:', count)
    try:
        dir = folderpath
        for x in os.listdir(dir):
            print("\n           Deleting ",x)
            os.remove(os.path.join(dir, x))
        print("\n           Files Deleted Successfully!!           ")
    except Exception as e:
        print(e)

