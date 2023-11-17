import os


def file_counter(path):
    dir_list = os.listdir(path)
    for i in dir_list:
        if os.path.isdir(path + '\\' + i):
            file_counter(path+'\\'+i)
        else:
            print(path+'\\'+i)
    return


path = 'C:\Huion Tablet'
file_counter(path)
