
# Write a program in Python to display the first 10 natural numbers.
"""
Expected Output :

1 2 3 4 5 6 7 8 9 10
"""

start   = 1
end     =10

while (start <= 10):
    print(start, end=' ')
    start+=1

# Write a Python program to find the sum of first 10 natural numbers.
"""
Expected Output :

The first 10 natural number is :
1 2 3 4 5 6 7 8 9 10

The Sum is : 55
"""
print("\n")
start   = 1
end     = 10
sum = 0

print("The first 10 natural number is :")
while (start <= end):
    print(start, end=' ')
    sum += start
    start += 1
print("\nThe Sum is :", sum)


# Write a program in Python to display n terms of natural number and their sum.
"""
Test Data : 7

Expected Output :

The first 7 natural number is :
1 2 3 4 5 6 7

The Sum of Natural Number upto 7 terms : 28
"""

start   = 1
end     = int(input("How Many terms :"))
sum = 0
print("The first", end, "natural number is :")
while (start<=end):
    print(start, end=' ')
    sum = sum + start
    start += 1
print("\nThe Sum of Natural Number upto", end, "terms :",sum)

# Write a program in Python to read 10 numbers from keyboard and find their sum and average.

"""
Test Data :

Input the 10 numbers :
Number-1 :2
...
Number-10 :2
Expected Output :
The sum of 10 no is : 55
The Average is : 5.500000
"""

start =1
end = 10
sum = 0

while (start <= end):
    print("Number-", start, ":", end='')
    num = int(input())
    sum = sum +start
    start += 1
print("The sum of 10 no is :", sum)
print("The Average is : %.6f" %(sum/10))


# Write a program in Python to display the cube of the number upto given an integer.

"""
Test Data :
Input number of terms : 5

Expected Output :
Number is : 1 and cube of the 1 is :1
Number is : 2 and cube of the 2 is :8
Number is : 3 and cube of the 3 is :27
Number is : 4 and cube of the 4 is :64
Number is : 5 and cube of the 5 is :125
"""

start = 1
end = 5

while (start <= end):
    mul = start**3
    print("Number is :",start,"and cube of the 1 is :", mul)
    start+= 1

# Write a program in Python to display the multiplication table of a given integer.

"""
Test Data :
Input the number (Table to be calculated) : 15
Expected Output :
15 X 1 = 15
...
...
15 X 10 = 150
"""

num = int(input("Table To calculated: "))
start = 1
end = 10
while (start <= end):
    print(num,"X",start, "=",num*start )
    start += 1

# Write a program in Python to display the pattern like right angle triangle using an asterisk.

"""
The pattern like :
4
*
**
***
****
"""

start = 1
end = int(input("How Many Pattern like: "))

while (start<=end):
    for index in range(start):
        print("*", end= '')
    print()
    start+=1



