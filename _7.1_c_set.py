"""
Unordered
Unchangeable - but remove items and add new items
Unindexed
"""
# set Declare
# Process - 01
my_set = {1,2,3,(1,2)}
print(my_set)
print(type(my_set))

#Process - 02

my_set2 = set((1,2,"3","a"))
print(my_set2)

# Value Access

# Value Add
my_set2.add(10)
print(my_set2)
my_set.add('b')
print(my_set)

# Value Update
my_set.update([1,2,3,4,5,6, 'ab'])
print(my_set)
my_set2.update([2,3,6,7,'xy'])
print(my_set2)


"""
Delate Value
দুই ভাবে ডিলিট করা যায়। যেমন:
discard()
remove()
"""
# Discard Value
my_set3 = {1,2,3,4,5}
print(my_set3)
my_set3.discard(2)
print(my_set3)
# Remove Value
my_set3.remove(4)
print(my_set3)

"""
Union (|), Intersection (&) and Defference (-)
"""
a = {1, 2, 3, 4, 4, 4, 5, 6}
b = {4, 4, 5, 6, 7, 8, 9}


uni = a | b
inter = a & b
defer = a - b
print("union:", uni)
print("intersection: ", inter)
print("Defference: ", defer)







