print("Hello, world!")
#Variables
name = "world"
age = 18
print(f"My name is {name} and I am {age} years old.")

#Data Types
num = 42
str_var = "Python is fun!"
bool_var = True

#Printing Data types
print(f"\nNumber: {num}")
print(f"String: {str_var}")
print(f"Boolean: {bool_var}\n")

#Basic Operations
x = 10
y = 5
print(x + y)  # Output: 15
print(x - y)  # Output: 9
print(x * y)  # Output: 50

#Division & Modulo
division_result = x / y
modulo_result = x % y
print(f"Division Result: {division_result}")   #Output:  2.0
print(f"Modulo Result: {modulo_result}")      #Output:    0

#Exponents & Square Root
base = 9
exponent = 3
squareRootBase = 16

powerResult = base ** exponent
sqrtResult = squareRootBase ** 0.5

print(f"\nPower of Base {base} to the Exponent {exponent}: {powerResult}")    #Output: powerResult=729
print(f"Square root of {squareRootBase}: {sqrtResult}")                                                 #Output: sqrtResult=4

#Conditional Statements
x = 10
if x > 5:
    print("x is greater than 5")

#Loops
for i in range(5):
    print(i)
#Functions
def greet(name):
    print("Hello, " + name + "!")

greet("Alice")
