#set comprehension

#general structure of set comprehension
#{expression for item in iterable condition}

#clssswork
#create a set from list containing the natural numbers less than 100
#take only prime numbers and find in a set

# def prime_number(n):
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True
# prime_num_set = {i for i in range(2, 100) if prime_number(i)}
# print(prime_num_set)


prime_number = {i for i in range(2, 100) if all(i % j != 0 for j in range(2,i))}
print(prime_number)
