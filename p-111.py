import os
import shutil

source = "C:/Users/angel/Downloads"
destination = "C:/Users/angel/OneDrive/Desktop"

list_of_files = os.listdir(source)
print(list_of_files)

for i in list_of_files:
    root,ext = os.path.splitext(i)
    print("The root of the file is", root)
    print("The ext of the file is", ext)