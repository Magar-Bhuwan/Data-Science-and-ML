#Data Comprehension in python

#list comprehension

listing = [i for i in range(5)]
[0] #first element
[1] #second element [0,1]
[2] #third element [0,1,2]
[3] #fourth element [0,1,2,3]
[4] #fifth element [0,1,2,3,4]

print(listing)


#create a list of even numbers less than or equal to 10
result_list = [i for i in range(11) if i % 2 == 0]
print(result_list)

#general structure of data comprehension
# [expression iteration condition]

#classwork
#create a list of odd numbers less than or equal to 10

result_list = [i for i in range(11) if i % 2 != 0]
print(result_list)



#there is list containing the names
name_list = ['Ashish', 'Ajay', 'Aayush', 'Shyam', 'Ram']
#create a list of name starting with A
#create a list containing name that start wiht A 
#hint .startwith('A')
result_list = [i for i in name_list if i.startswith('A')]
print(result_list)



