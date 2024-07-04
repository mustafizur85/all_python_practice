"""
Key: value
key always unique
changeable
"""

# Dictionary Declare
# Process 01
my_dict = {}
print(type(my_dict)) # output: <class 'dict'>
print(my_dict) # output: {}

# Process 02
my_dict_2 = dict()
print(type(my_dict_2)) # output:  <class 'dict'>
print(my_dict_2) # output: {}

my_dict = {
    "name"          :    ["maisha Rahman", "Mehenaf Rahman"],
    "courseName"    :    "Python",
    "rollNumber"    :    154253,
    1               :    505,
    "permissionId"  :   [1,2,3,4,5],
    2               :   505

}
# indexing Flow
print(my_dict["name"][0]) # output: maisha Rahman
print(my_dict.get("name")) # output: ['maisha Rahman', 'Mehenaf Rahman']
print(my_dict.get("age"))  # None
#print(my_dict.get["age"]) # KeyError: "age"


my_dict["name"] = "Mahmud Hasan"
print(my_dict)
my_dict ["age"] = 27
print(my_dict)

my_dict.pop("name")
print(my_dict)

my_dict.clear()
print(my_dict)



