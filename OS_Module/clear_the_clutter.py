# A Python utility that automatically renames PNG files inside a folder in sequential order using the OS module.

import os

i = 1
files = os.listdir("cluttered_folder")
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"cluttered_folder/{file}",f"cluttered_folder/{i}.png")
        i = i+1

