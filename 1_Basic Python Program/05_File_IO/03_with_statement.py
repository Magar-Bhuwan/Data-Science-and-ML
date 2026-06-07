#with statement

with open("file2.txt","w") as file:
    file.write("Hello! Good Morning")


with open("file2.txt", "r") as file:
    print(file.read())

with open("file2.txt", "a") as file:
    file.write("Welcome to the world of Python")