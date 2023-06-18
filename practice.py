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
