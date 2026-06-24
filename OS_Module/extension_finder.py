# A file categorization tool that scans a directory and groups files based on their extensions such as .py, .txt, and .png.

import os

files = os.listdir("cluttered_folder")


python_files = []
text_files = []
png_files = []

for file in files:
    if file.lower().endswith(".py"):
        python_files.append(file)
    elif file.lower().endswith(".png"):
        png_files.append(file)
    elif file.lower().endswith(".txt"):
        text_files.append(file)
print("Python Files:")
for file in python_files:
    print(file)

print("\nText Files")
for file in text_files:
    print(file)

print("\nPNG Files")
for file in png_files:
    print(file)
