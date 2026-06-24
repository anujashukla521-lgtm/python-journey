# A Python automation script that organizes files into separate folders based on their extensions, such as Images, Documents, and Python Files.

import os

files = os.listdir("cluttered_folder")

folder_name = "Images"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
else:
    print(f"{folder_name} already exists")

folder_name = "Documents"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
else:
    print(f"{folder_name} already exists")

folder_name = "Python_Files"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
else:
    print(f"{folder_name} already exists")



for file in files:
    if file.lower().endswith(".png"):
        old_path = os.path.join("cluttered_folder",file)
        new_path = os.path.join("Images",file)
        os.rename(old_path,new_path)
        print(f"Moved {file} to Images")

    elif file.lower().endswith(".py"):
        old_path = os.path.join("cluttered_folder",file)
        new_path = os.path.join("Python_Files",file)
        os.rename(old_path,new_path)
        print(f"Moved {file} to python folder")
      

    elif file.lower().endswith(".txt"):
        old_path = os.path.join("cluttered_folder",file)
        new_path = os.path.join("Documents",file)
        os.rename(old_path,new_path)
        print(f"Moved {file} to documents")