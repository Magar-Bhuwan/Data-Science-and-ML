# password checker file handling 

# with open('password.txt', 'w') as f:
#     f.write('\n ram@123 \n shyam@123 \n hari@123')


# with open('password.txt', 'r') as f:
#     data = f.readlines()

#     data = [line.strip() for line in data]

#     user_input = input("Enter your password: ").strip()
#     try:
#         if(user_input in data):
#             print("password is present")
#         else:
#             print("password is not present")
#     except Exception as e:
#         print(e)

try:
    with open('password.txt', 'w') as f:
        f.write('Ram@123\nShyam@123\nHari@123\nGita@123')

except PermissionError:
    print("Error: No permission to write 'password.txt'.")
    exit(1)

except OSError as e:
    print(f"Error writing file: {e}")
    exit(1)

try:
    with open('password.txt', 'r') as f:
        data = [line.strip() for line in f if line.strip()]

except FileNotFoundError:
    print("Error: 'password.txt' not found.")
    exit(1)

except PermissionError:
    print("Error: No permission to read 'password.txt'.")
    exit(1)

except OSError as e:
    print(f"Error reading file: {e}")
    exit(1)

try:
    user_input = input("Enter your password: ").strip()
except (EOFError, KeyboardInterrupt):
    print("\nInput cancelled.")
    exit(0)

if not user_input:
    print("Error: Password cannot be empty.")
    exit(1)

if user_input in data:
    print("Password is present.")

else:
    print("Password is not present.")

