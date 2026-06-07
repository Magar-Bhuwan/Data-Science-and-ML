# ============================================================
# Chapter 1 - Strings
# Topics: String methods, slicing, f-strings, type casting,
#         for loop with range, palindrome check
# ============================================================

# --- String Methods ---
# name = input("Enter the messages to the system: ")
# print(name)
# print(name.upper())
# print(name.capitalize())
# print(name.title())
# print(len(name))

# --- F-String ---
# age = 20
# print(f'my name is {name} and i am {age} years old')

# --- Indexing & Slicing ---
# print(name[5])
# print(name[0:4])

# --- Type Casting ---
# a = "123"
# num = int(a)
# print(num)
# print(type(num))

# --- Reverse a String ---
# a = "Python"
# print(a[::-1])
# count = len(a)
# print(count)

# --- Palindrome Check ---
# text = input("Enter the text: ")
# if text == text[::-1]:
#     print("It's a palindrome.")
# else:
#     print("It's not a palindrome.")

# --- For Loop with Range ---
a = input("Enter the text: ")
for i in range(1, 101):
    print(f"{i}: {a}")
