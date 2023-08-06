def greet(name):
    print("Hello, " + name + ". Good morning!")

def absolute_value(num):
    if num >= 0:
        return num
    else:
        return -num

def my_func():
    x = 10
	print("Value inside function:",x)

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
