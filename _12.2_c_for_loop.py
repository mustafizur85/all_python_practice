"""
In Programing, you often want to execute a block of code multiple times. To do so, you use a for loop.
Use the for loop statement to run a code block a fixed number of times.
Use the range (start, stop, step) to customize the loop.
"""
# for Loop syntex
"""
for index in range(n)
    statement
"""
print("Aproce - 01")
for index in range(10):
    print(index)

print("Aproce - 02")
for index in range(0,10):
    print(index)

print("Aproce - 03")
for index in range(1,10):
    print(index)

print("Aproce - 04")
for index in range(0, 10, 2):
    print(index)



# Using Python for loop to calculate the sum of a sequence.
print("Sequence of Sum Aproce - 01 :")
sum = 0
for num in range(10):
    sum+= num
    print(sum)


print("Sequence of Sum Aproce - 02 :")
sum = 0
for num in range(10):
    sum+= num # sum = sum + num
print(sum)

print("Sequence of Sum Aproce - 03 :")
sum = 0
for num in range(10, 20):
    sum+= num
    print(sum)