
"""
python এ মুলত দুই ধরনের loop হয় যেমন:
(i) for loop
(ii) while loop
Loop use করা হয় একই জিনিস বার বার আনার জন্য।
looping করার সময় তিনটি জিনিস খেয়াল রাখতে হবে....
(1) End Value
(2) Start Value
(3) step(incriment & decriment)
"""
# While loop syntex
"""
while (condition):
    block of Code
incriment/ decriment
"""
"""
# Aprose 01
print("Aprose 01 :")
start = 1
while start<=8:
    print("Hello Word")
    start += 1

# Aprose 02
print("Aprose 02 :")
end = 5
start = 1
while start<=end:
    print("Hello Word")
    start += 1

# Aprose 03
print("Aprose 03 :")
end = 5
start = 1
while start<= end:
    print(start)
    start += 1

# Aprose 04
print("Aprose 04 :")
num_of_rept = int(input("How Many times to Your Rept: "))
start = 1
while start <= num_of_rept:
    print("I Love My Country")
    start+= 1

# Aprose 05
print("Aprose 05 :")
num_of_rept = int(input("How Many times to Your Rept: "))
start = 1
while start <= num_of_rept:
    print(start)
    start+= 1

# Aprose 06
print("Aprose 06 :")
num_of_rept = int(input("How Many times to Your Rept: "))
start = 1
while start <= num_of_rept:
    # Block of Code
    num1 = 10
    num2 = 20
    result = num1 + num2
    print(result)
    start+= 1

# Aprose 07
print("Aprose 07 :")
num_of_rept = int(input("How Many times to Your Rept: "))
start = 1
while start <= num_of_rept:
    # Block of Code
    num1 = int(input("Enter Your First Number: "))
    num2 = int(input("Enter Your 2nd Number: "))
    result = num1 + num2
    print(result)
    start+= 1
"""

# 1 - 99 পর্যন্ত বিজোড় সংখ্যা বের কর।
# Aprose 08
print("Aprose 08 ( Odd Number 1 - 99) :")
end     = 99
start   = 1

while (start<=end):
    if (start % 2==1):
        print(start)
    start+= 1


# 2 - 100 পর্যন্ত বিজোড় সংখ্যা বের কর।
# Aprose 09
print("Aprose 09 ( Even Number 2 - 100) ")
end     =   100
start   =   1

while (start<=end):
    if(start % 2 == 0):
        print(start)
    start+= 1

# 2 - 100 পর্যন্ত বিজোড় সংখ্যা বের কর।
# Aprose 09
# Dainamic
print("Aprose 09 ( Even Number) ")
end     =   int(input("How Many times looping :"))
start   =   1

while (start<=end):
    if(start % 2 == 0):
        print(start)
    start+= 1

# 2 - 100 পর্যন্ত বিজোড় সংখ্যা বের কর।
# Aprose 10
# Dainamic
print("Aprose 09 ( Odd Number) :")
end     =   int(input("How Many times looping :"))
start   =   1

while (start<=end):
    if(start % 2 == 1):
        print(start)
    start+= 1



