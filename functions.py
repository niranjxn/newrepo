
# 6. Functions
def greet(name):
   return f"Hello, {name}! Welcome to Python."
def calculate_area(length, width):
   area = length * width
   return area
def introduce(name, age, city="Unknown"):
   return f"Name: {name}, Age: {age}, City: {city}"
print(greet("Alice"))
print(f"Area of rectangle: {calculate_area(10, 5)}")
print(introduce("Bob", 25))
print(introduce("Charlie", 30, "London"))
def circle_calculations(radius):
   diameter = 2 * radius
   circumference = 2 * 3.14159 * radius
   area = 3.14159 * radius ** 2
   return diameter, circumference, area
d, c, a = circle_calculations(7)
print(f"Circle with radius 7: Diameter={d}, Circumference={c:.2f}, Area={a:.2f}")
