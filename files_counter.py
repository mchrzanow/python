import os

dirname ='C:\Huion Tablet'

def file_counter(path):
    dir_list=os.listdir(path)
    num_files=0
    for f in dir_list:
        if os.path.isfile(os.path.join(path, f)):
            num_files +=1

    return num_files

print(file_counter(dirname))