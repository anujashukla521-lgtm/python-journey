import shutil
import os

zip_name = os.path.join("shutil-module","Project_Backup")
shutil.make_archive(zip_name,'zip','shutil-module/Project')

