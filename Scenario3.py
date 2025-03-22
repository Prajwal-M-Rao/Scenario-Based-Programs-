#Scenario 3:Write a program to check the type of triangle based on the sides provided.

# Input: Lengths of three sides of a triangle

#  Conditions:
#  If all sides are equal, it's an Equilateral triangle.
#  If two sides are equal, it's an Isosceles triangle.
#  If no sides are equal, it's a Scalene triangle.

print("Enter the sides of the triangle: ")
a=int(input("A: "))
b=int(input("B: "))
c=int(input("C: "))
if a==b==c:
    print("Equilateral Triangle")
elif a==b or b==c or c==a:
    print("Isosceles Triangle ")
else:print("Scalence Triangle")