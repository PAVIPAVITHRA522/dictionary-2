"""16.write a python program to sum all the dictionary values without using sum function """
d = {"a":34,"b":45,"c":50,"d":34,"e":100}
print("original dictionary: ",d)
s = 0
for val in d.values():
    s += val
print("summation of all values: ",s)

"""17.write a python program to transform a dictionary into list of tuples"""
d = {"a":34,"b":45,"c":50,"d":34,"e":100}
item_list = []
for item in d.items():
    item_list.append(item)
print("output list is :",item_list)
"""18.write a python program to find size of dictionary"""
from sys import getsizeof
d = {"a":34,"b":45,"c":50,"d":34,"e":100}
size_dict = getsizeof(d)
print("size of dictionary in bytes: ",size_dict)

"""19 create dictionary with key value pairs and then change values of particular key"""
d = {"a":34,"b":45,"c":50,"d":34,"e":100}
print("original dictionary is: ",d)

d["a"] = 999
print("updated dictionary is: ",d)

"""20 write a program user will enter its details like name,age ...etc,create one dictionary for that and display readable information on the console of that user"""
name,age,city = input("enter name,age and city: ").split()
d = {}
d["name"] = name
d["age"] = int(age)
d["city"] = city
print(d)
print("your information is followed as follows")

print("name is: ",d["name"])
print("age is: ",d["name"])
print("city is: ",d["city"])


