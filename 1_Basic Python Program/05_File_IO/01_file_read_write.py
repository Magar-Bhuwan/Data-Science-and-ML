# # read file
# file = open('file1.txt','r')                #read file
# print(file.read())
# print(type(file))
# file.close()

#write file

file = open("D:\\ML with Python\\Data Seience & ML\\COURSE\\file IO\\file1.txt","w")
file.write(" Welcome! to the world of Python.")
print(type(file))
file.close()

#append file

file = open("D:\\ML with Python\\Data Seience & ML\\COURSE\\file IO\\file1.txt","a")
file.write("Hello! Good Morning")
file.close()
