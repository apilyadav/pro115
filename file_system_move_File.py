import os
import shutil
from_dir="C:/Users/Lenovo/Downloads"
to_dir="C:/Users/Lenovo/Desktop"
#Source file path
source = 'main.txt'
# destination file path
dest = 'newfile.txt'
os.rename(source,dest)
print("rename succesfully")