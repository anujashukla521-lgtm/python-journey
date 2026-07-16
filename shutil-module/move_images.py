import os
import shutil

source_folder = "shutil-module/Project"
destination_folder = "shutil-module/Images"

os.makedirs(destination_folder, exist_ok=True)

for file in os.listdir(source_folder):
    if file.lower().endswith((".jpg", ".png")):
        source = os.path.join(source_folder, file)
        shutil.move(source, destination_folder)

print("All image files moved successfully!")