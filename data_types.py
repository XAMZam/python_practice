#variable types
#Integers, floating-point numbers and complex numbers fall under Python numbers category. 
#They are defined as int, float and complex classes in Python
# int-holds signed integers of non-limited length.
print(123456)

#float-holds floating decimal points and it's accurate up to 15 decimal places.
print(3.56789)

#Complex-holds complex numbers.
print(1+2j)






#string-is a sequence of characters represented by either single or double quotes
print('Hello world')
print("Zamzam Ali Hedar")
#boolean
print(True)
print(False)




#list- is an ordered collection of similar or different types of items separated by commas and enclosed within brackets [ ].
#you can change the value once stored.

#listing slicing
x= [1,2,3,4,5]
print(x[0])  # This will print the first element (index 0)
print(x[2])  # This will print the third element (index 2)
print(x)  # This will print the updated list


Countries = 'Togo,Cameroon,Uganda'
print(Countries[0])


#tuple- A tuple is an ordered sequence of items same as a list. 
#The only difference is that tuples are immutable. Tuples once created cannot be modified.
products = 'x-box,microsoft,google'
product_list = products.split(',')  # Split the string by comma into a list
print(product_list[0])  # Print the first element of the list



#dict-is an ordered collection of items. It stores elements in key/value pairs.
#keys- name,age,contry
#values- Zamzam,Togo
x= {'name':'Zamzam','age':20,'country':'Togo'}

#set- is an unordered collection of unique items. 
#Set is defined by values separated by commas inside braces { }.
student_id= {114,116,118,121}
print(student_id)
print(type(student_id))


