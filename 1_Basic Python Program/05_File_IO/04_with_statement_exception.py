try:
    with open('file2.txt', 'r') as file:
        print(file.read())

except FileNotFoundError:
    print("Error found")

