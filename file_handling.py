# 8. File Handling
#####################
with open("sample.txt", "w") as file:
   file.write("Hello, File World!\n")
   file.write("This is a second line.\n")
   file.write("Python is awesome!\n")
print("File written successfully!")
print("\nReading file content:")
with open("sample.txt", "r") as file:
   content = file.read()
   print(content)
print("Reading line by line:")
with open("sample.txt", "r") as file:
   for line_number, line in enumerate(file, 1):
       print(f"Line {line_number}: {line.strip()}")
with open("sample.txt", "a") as file:
   file.write("This line was appended later.\n")
print("\nFile after appending:")
with open("sample.txt", "r") as file:
   print(file.read())