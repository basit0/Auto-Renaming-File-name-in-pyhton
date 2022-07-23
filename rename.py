import os
from append import append_multiple_lines
path =os.chdir("C:\\Users\\basit\\Desktop\\rename\\py_rename-master\\test")
value =1
tex_file =[]
for file in os.listdir(path):
    new_file_name ="fileh{}.csv".format(value)
    os.rename(file , new_file_name)
    k = "fileh" + str(value) + ".csv"
    data = tex_file.append(k)
    print(k)

    value =value +1
print(tex_file)
append_multiple_lines("C:\\Users\\basit\\Desktop\\rename\\py_rename-master\\filename.txt",tex_file)
