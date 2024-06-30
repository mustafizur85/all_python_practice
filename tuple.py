
#Tuple ------> Order, Unchageable, Allow Duplicate

#tuple Declare:

# Processes - 01
tuple1 = ()
# Processes - 02
tuple2 = tuple((1,2,3,"python"))

#Data Type Check

print(type(tuple1)) # <class 'tuple'>
print(type(tuple2)) # <class 'tuple'>

#Accessing of tuple:

tpl3 = (1,2,3,"python",5,6)
print(tpl3[0])
print(tpl3[-1])
print(tpl3[0:])
print(tpl3[0:2])
print(tpl3[0:-2])
print(tpl3[:6])
print(tpl3[-3:-1])

tpl4 = tuple((1,2,3,4,5,6))
print(tpl4[0])
print(tpl4[0:5])
print(tpl4[5])
print(tpl4[-5])
print(tpl4[-5:])

# Connate
tpl5 = (1,2,3)
tpl6 = tpl3+tpl5
print(tpl6)