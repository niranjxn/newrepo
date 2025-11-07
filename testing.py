# 1. Welcome Message and Area of Circle
#####################
print("Welcome to Python Programming!")
# Calculate area of a circle
radius = 5
area = 3.14159 * radius ** 2
print(f"Area of circle with radius {radius} is: {area:.2f}")
# Simple user interaction
user_name = input("Please enter your name: ")
print(f"Hello, {user_name}! Let's learn Python together!")

#####################
# 2. Variables, Data Types, Lists, and Dictionary
#####################
name = "John Doe"
message = 'Hello, World!'
multiline_text = """This is a
multi-line string"""
# Numbers
age = 25
price = 19.99
is_student = True
# Lists
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
# Dictionary
person = {
   "name": "Alice",
   "age": 30,
   "city": "New York"
}
print(f"Name: {name}, Age: {age}")
print(f"Fruits: {fruits}")
print(f"Person: {person}")

#####################
# 3. Arithmetic and String Operations
#####################
a = 10
b = 3
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b:.2f}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Exponent: {a} ** {b} = {a ** b}")
print(f"Modulus: {a} % {b} = {a % b}")
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")
print(f"Name in uppercase: {full_name.upper()}")
print(f"Name length: {len(full_name)}")

#####################
# 4. If-Elif-Else Conditions
#####################
temperature = 25
if temperature > 30:
   print("It's hot outside!")
elif temperature > 20:
   print("The weather is pleasant.")
elif temperature > 10:
   print("It's a bit chilly.")
else:
   print("It's cold outside!")
age = 18
has_license = True
if age >= 18 and has_license:
   print("You can drive!")
else:
   print("You cannot drive.")
score = 85
if score >= 90:
   grade = "A"
elif score >= 80:
   grade = "B"
elif score >= 70:
   grade = "C"
elif score >= 60:
   grade = "D"
else:
   grade = "F"
print(f"Score: {score}, Grade: {grade}")



#####################
