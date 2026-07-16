import shutil

shutil.copytree(
    "shutil-module/Project",
    "shutil-module/Backup_Project",
    dirs_exist_ok=True
)