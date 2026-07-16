import shutil
import os

folder = "shutil-module/TempFolder"

try:
    if os.path.isdir(folder):
        shutil.rmtree(folder)
        print("Folder deleted successfully.")
    else:
        print("Folder not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"Error: {e}")