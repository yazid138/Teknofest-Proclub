#FROM ex21.py LEARN PYTHON THE HARDWAY
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Let's do some math with just functions!")
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

#Printing age height weight and iq
print(age, height, weight, iq)

print("Here is a puzzle.")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
#Printing what
print(what)
