# print("This is try except example")
# try:
#     if user is not int:
#         print("THis runs...!!!")
# except Exception as e:
#     print(e)

# print("this is after error code")
# f = open("sample.txt", "a")
# f.write("\nHello python") 
# # print(f.read())
# f.close()
import os
from packages import DeleteFilesInsideFolder , DeleteSpecificFile , ShowFiles
def DeleteProgram():
    print("\n           DELETE THE FILES           ")

    choose = int(input("\n           [1] Delete All files from folder\n           [2] Delete single file\n           [3] Exit\n           Enter you choice: "))


    if choose == 1:
        folder_path = input("\n           Enter the folder path: ")
        DeleteFilesInsideFolder.DeleteInsideFolder(folderpath=folder_path)
    elif choose == 2:
        file_path = input("\n           Enter the file path: ")
        DeleteSpecificFile.DeleteSingleFile(filepath=file_path)
    elif choose == 3:
        exit("\n            .\n            .\n            .\n            .\n            .\n            .\n            .\n            .\n            .\n            .\n            Thanks for using...\n           ")
    else:
        print("Error!")
        exit()

DeleteProgram()

def RunAgain():
    doyou = input("\n           Want to use this program again 'yes' or 'no' : ")
    if doyou == 'yes':
        DeleteProgram()
    elif doyou == 'no':
        exit("\n            .\n            .\n            .\n            .\n            .\n            .\n            .\n            .\n            .\n            .\n            Thanks for using...\n           ")
    else:
        exit("\n            .\n            .\n            .\n            .\n            .\n            .\n            .\n            .\n            .\n            .\n            Thanks for using...\n           ")

RunAgain()