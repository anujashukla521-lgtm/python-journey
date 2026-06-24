import os

for i in range(1, 11):
    folder_name = f"Day{i}"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    else:
       print(f"{folder_name} already exists")
   
