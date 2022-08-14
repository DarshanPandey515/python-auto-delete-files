import os


def DeleteSingleFile(filepath):
    try:
        file = filepath
        os.remove("\n           Deleting ",file)
        print("\n           File Deleted Successfully!!           ")
    except Exception as e:
        print(e)