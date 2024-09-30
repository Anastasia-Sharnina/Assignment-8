# Input: three integer variables
a = int(input("Enter first integer (a): "))
b = int(input("Enter second integer (b): "))
c = int(input("Enter third integer (c): "))

# Sorting using simple if statements
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

# Output the sorted values
print(a, b, c)
