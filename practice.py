import keyword

# different type variables declared
print("Hello World")
a = 123
print(a)
s = 'a'
t = "Hello"
print(s)
print(t)
m = True
print(m)
n = None
print(n)

#all reserved keyword for pythorn
print(keyword.kwlist)

#type
hello = 55.35
print(type(hello))

pi = 3.14
print(type(pi))

a, b, c = 1, 2, 3
print(a, b, c)

a, b , _ = 1, 2, 3
print(a, b)
print(_)

#list
x = y = [10, 20, 20]
print(x)
z = [10, 20, [19, 20, 24], 33]
print(z[2])

#basic function declaration  
def my_function(x):
    a = x + 5
    return a
print (my_function(10))

#if else statement
if(pi > 10):
    print("pi is greater")
else:
    print("10 is greater")

floatNumber = 10 + 10J
print(floatNumber)


#conditional Statement Checking instance
i = 10
if isinstance(i, int):
    i += 10
elif isinstance(i, str):
    i += 20
print(i)

#Collections 
array = ['Apple', 'Orange', 'Banana', 'Coconut']
array.append(['Nahad', 2])
array.insert(2, 'Foyaz')
array.remove('Orange')
print(array)

#reverse
listOfAnimal = ['Tiger', 'Lion', 'Hen', 'Elephent']
listOfNumber = [2, 5, 8]
listOfAnimal.reverse()
#or
listOfNumber[::-1]
#remove last element
listOfNumber.pop()
print(listOfAnimal)
print(listOfNumber)

#iteration
for element in listOfAnimal:
    print(element)

#tuple
ip_address= ("100.10.10.101", 8080)
print (ip_address)
