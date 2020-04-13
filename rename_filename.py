import os

# import shutil
#
# shutil.rmtree("file_rename_test")  # 能删除该文件夹和文件夹下所有文件
# os.mkdir("file_rename_test")


# os.mkdir("file_rename_test")
# os.chdir("file_rename_test")
#
#
# for i in range(10):
#     f=open("ceshi%d.txt" % i, 'w')
#     f.close()

# os.chdir("file_rename_test")
# os.


os.chdir("file_rename_test")
my_list = os.listdir()

for file_name in my_list:
    new_file_name = file_name.replace(".txt","heiha.txt")
    print(new_file_name)
    os.rename(file_name,new_file_name)