#Task 1: Calculate Factorial Using a Function
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("Enter the number:"))
result=factorial(num)
print(result)

#Task 2: Using the Math Module for Calculations
import math
num=int(input("Enter the number:"))
square_root=math.sqrt(num)
logarithm=math.log(num)
sine=math.sin(math.radians(num))
print("square_root:",square_root)
print("logarithm:",logarithm)
print("sine:",sine)
