import shutil 
import os

folder_name = "shutil-module/Documents"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

shutil.move("shutil-module/report.pdf",folder_name)