# what is exception handling?

#try-except blck
#try-except-else block
#try-except-else-finally block

#example

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter a number: "))
#     print(a/b)
# # except:
# #     print("some error occured")

# except ValueError:
#     print("invalid input")

# except ZeroDivisionError:
#     print("cannot divide by zero")

# except Exception as e:
#     print(e)


#classwork
# create a function that takes two numbers as input and returns their sum
#use try-except block to handle the case where the input is not a number

def func(n1, n2):
    try:
        return n1 + n2
    
    except TypeError:
        print("invalid input")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
print(func(num1, num2))


