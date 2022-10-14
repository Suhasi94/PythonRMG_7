import os
path = r"C:\Users\User\OneDrive\Desktop\filehandling\files"
os.chdir(path)
# without context  manager
#file_obj=open("sample.txt","r")
#print(file_obj.read())
#print(file_obj.readline())
#print(file_obj.readlines())

#print(file_obj.read(17))
#print(file_obj.readlines(34))
#print(file_obj.closed)
#print(file_obj.readable())
#print(file_obj.writable())
#file_obj.close()

#file_obj=open("sample.txt","w")
#file_obj.write("hello")
#file_obj.close()

# with context manager
"""
with open("sample.txt","r") as file:
    #print(file.read())
    print(file.readline())
    print(file.readlines())
    print(file.closed)
print(file.closed)


with open("sample1.txt","a") as file:
    print(file.write("hello python\n"))
    print(file.write("programming\n"))
    file.writelines(["welcome\n","python programming\n","hello world\n"])

with open("sample2.txt","x") as file:
    file.write("hello")

with open("sample1.txt","r") as file:
    print(file.read())
    file.seek(0)
    print(file.readline())


with open("sample1.txt","r") as file:
    for line in file:
        print(line)

"""







    
























































