# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter a number: "))
#     result = a/b

# except ZeroDivisionError:
#     print("cannot divide by zero")

# #else always runs if try block will run
# else:
#     print(f"Result = {result}")

# #finally always runs if there is exception or not
# finally:
#     print("This is always executed")


#classwork
# create a function that takes any kind of iterable as input
# and try to reverse it
# use try-except-else-finally block to handle the case where the input is not an iterable

def rev_num(iterable):
    error_type = None
    message = None

    try:
        result = iterable[::-1]
    
    except TypeError:
        error_type = "type error"
        message = "invalid input"

    else:
        print(f"successfully reversed {result}")

    finally:
        if error_type:
            print(f'{error_type} : {message}') 
        else:
            print (result)

print(rev_num([1,2,3,4,5]))