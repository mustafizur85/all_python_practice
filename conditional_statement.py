# Python hs six conditional statement that are used in decesion making:-
"""
1. if the statement
2. if else statement
3. nested if statement
4. if...elif ladder
5. short hand if statement
6. short hand if-else statement
"""
# Relation Oparator
"""
< less than
<= less than equal to
> greater than
>= greater than equal to
== equal to
!= not equal to
"""
# Conditional Logic
"""

if(condition):
    code
elif:
    code
else:
    code
"""

# বিজোড় বা জোড় সংখ্যা বের করার conditional logic:

user_input = int(input("Enter Your any Number: "))
remainder = user_input % 2

if(remainder == 0):
    print("Even Number")
else:
    print("Odd Number")

# Nested if :
user_input1 = int(input("Enter Your any Number: "))
remainder1 = user_input1 % 2
if(remainder1 == 0):
    print("Even Number")
    if(remainder1 == 0):
        print("Odd Number")
    else:
     print("Nothing")
"""
 প্রশ্ন: ইউজার যে ইনপুট দিবে তা যদি zero এর চেয়ে বড় হয় তাহলে print হবে Positive,  
যদি zero এর চেয়ে ছোট হয় তাহলে print হবে Negative আর যদি zero এর সমান হয় তাহলে print হবে Number is Zero 
অন্যথায় print হবে Nothing
"""

user_input2 = int(input("Enter Your Number: "))
if(user_input2 > 0):
    print("Positive")
elif(user_input2 < 0):
    print("Negative")
elif(user_input2 == 0):
    print("Number is Zero")
else:
    print("Nothing")

