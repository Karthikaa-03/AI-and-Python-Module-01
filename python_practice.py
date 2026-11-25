# Module 01: Beginner Python Practice
# Run: python python_practice.py

print("1. Welcome program")
name = input("Enter your name: ")
print("Welcome,", name)

print("\n2. Add two numbers")
a = 10
b = 20
print("Sum =", a + b)

print("\n3. Check even or odd")
number = 7
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

print("\n4. Print numbers using a loop")
for i in range(1, 6):
    print(i)

print("\n5. Function example")
def square(value):
    return value * value

print("Square of 4 =", square(4))

print("\n6. List example")
subjects = ["Python", "Java", "Artificial Intelligence"]
for subject in subjects:
    print(subject)
