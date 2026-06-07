#dictionary comprehension

#general structure of dict comprehension
# {key:value for item in iterable condition}

square_dict = {i:i*i for i in range(5)}
print(square_dict)


#classwork
#create a dictionary from strring "hello world"
#the key should be the character and the value should be the count of the character 
#the string is "hello world"

text = "hello world"

dict_comp = {i:text.count(i) for i in text if i != ' '}
print(dict_comp)

#create a dict from list of strings
#the key should be the string and the value should be the length of the string
#the list is ['hello','world','python','java']

dict_list = ['hello','world','python','java']
dict_comp = {i:len(i) for i in dict_list}
print(dict_comp)
