import shutil

total, used, free = shutil.disk_usage("shutil-module")

print(f"Total Space : {total / (1024**3):.2f} GB")
print(f"Used Space  : {used / (1024**3):.2f} GB")
print(f"Free Space  : {free / (1024**3):.2f} GB")