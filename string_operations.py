var = 'PowerLearnProject'
result = var[5]   #single
result = var[0:8] #multiple,you can also use [:8]/it will autimatically know about the zero.
result= var[5:]
print(result)

#numbers in str
var = 'PowerLearnProject'
print(len(var))


#exercise 1-It's a great sunday
var1 = 'It\'s Sunday'
var2 = 'Have a great day'
print(var1[:5]+ var2[5:13]+var1[5:])

#exercise 2 *a=200,b=100
a= 100
b=200
c=a
a=b
b=c
print(a,b)

