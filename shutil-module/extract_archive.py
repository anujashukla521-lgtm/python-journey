import shutil
import os

filename = os.path.join("shutil-module","Project_Backup.zip")
extract_dir = os.path.join("shutil-module","Recovered_Folder")

shutil.unpack_archive(filename,extract_dir)
print("Archive extracted successfully!")