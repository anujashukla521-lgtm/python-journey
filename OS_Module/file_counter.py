import os

files = os.listdir("cluttered_folder")

file_count = 0
folder_count = 0
for item in files:
    path = os.path.join("cluttered_folder", item)
    if os.path.isfile(path):
        file_count+=1
    elif os.path.isdir(path):
        folder_count+=1

print(f"Files: {file_count}")
print(f"Folders: {folder_count}")