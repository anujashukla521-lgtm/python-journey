import shutil 

try:
    shutil.copy("shutil-module/notes.txt","shutil-module/backup_notes.txt")
    print("File copied successfully")
except FileNotFoundError:
    print("Source file not found")