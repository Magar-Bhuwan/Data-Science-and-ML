# count the numbers of words in file:

# with open('file1.txt', 'r') as file:
#     data = file.read()                      #got exhausted
#     print(len(file.read().split()))
#     print(type(file))
#     print(data)

# Calculate the number of lines in file
# with open('file1.txt', 'r') as file:
#     print(len(file.readlines()))

#check if 'python' word in present in file
with open('file1.txt', 'w') as file:
    file.write("Welcome to the world of python \n Hello! Good Morning")


with open('file1.txt', 'r') as file:
    data = file.read()
    if 'python' in data:
        print("python is present")
    else:
        print("python is not present")

