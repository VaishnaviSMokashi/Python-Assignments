#Task 1: Check if a Number is Even or Odd
num=int(input("Enter a number: "))
if num%2==0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

#Task 2: Sum of Integers from 1 to 50 Using a Loop
#for loop
total_sum=0
for i in range(1,51):
    total_sum+=i
print("The sum of 1 to 50 is:",total_sum)

#while loop
num1=1
total_sum1=0
while num1<=50:
    total_sum1+=num1
    num1+=1
print("The sum of 1 to 50 is:",total_sum1)

