import shutil 
import os

files = os.listdir("shutil-module/Project")

for file in files:
    if file.endswith(".txt"):
        source = os.path.join("shutil-module/Project",file)
        shutil.copy2(source,"shutil-module/Documents")