"""
local Scope
Golbal Scope
"""

#local scope

def getValue():
    x = 300
    print(x)

#global scope
y = 100

def printValue():
    print(y)

print(y)

# local scope থেকে global scope
def getNumber():
    global num1   #local scope এর মধ্যে যদি global key word ব্যবহার করা হয় তাহলে local scope, global হয়ে যায়।
    num1 = 1000
    print(num1)

getNumber()

print(num1)





