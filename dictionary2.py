"""6.write a program to sum values in that dictionary."""
num_dict = {"a":23,"b":45,"c":48}
result_sum = sum(num_dict.values())
print(result_sum)
#another way
num_dict = {"a":23,"b":45,"c":30}
result_sum = sum(num_dict.values())
print("sum is: ",result_sum)
result_sum_f = 0
for val in num_dict.values():
    result_sum_f += val
print("sum using for loop is: ",result_sum_f)

"""7.write a python program to sort a given dictionary by key."""
d = {"a":1,"b":2,"c":3}
print("original dictionary: ",d)
k = sorted(d.items())
print("final output dictionary: ",k)
#tuples into dictionery
d = {"a":1,"b":2,"c":3}
print("original dictionary: ",d)
k = dict(sorted(d.items()))
print("final output dictionary: ",k)

"""8.write a python program  to get the maximum and minimum values of a dictionary"""
d = {"a":80,"b":79,"c":89}
print("minimum value is: ",min(d.values()))
print("maximum value is: ",max(d.values()))

"""10.write a python program to get total number of items in that dictionary."""
d = {"a":18,"b":7,"c":9,"t":4,"f":6}
print("total number of items in d are: ",len(d))

"""11.write a python program to replace values of dictionary with sum of key and values."""
num_dict = {1:11,2:22,3:33,4:44,5:55}
print("original dictionary: ",num_dict)
for key,value in num_dict.items():
    num_dict[key]=key+value
print("output dictionary: ",num_dict)

"""12.write a python program ,take one list of words and create new dictionary its words are keys of that dictionary and values as length of the word"""
words_list = ["pune","bangalore","chennai","vellore"]
print("original list: ",words_list)
words_len_dict = {}
for words in words_list:
    words_len_dict[words] = len(words)
print("output dictionary: ",words_len_dict)

"""13 write python program to invert key,value pairs in a dictionarty."""
d ={"name":"ram","age":22,"address":"pune","salary":20000}
d1 = {}
for key,value in d.items():
    d1[value] = key
print("d1 is:",d1)
"""14.write a python program,take one numbers list and create new dictionary its key is number and value is square of that number from number list"""
num_list = list(range(1,11))
print("number list is: ",num_list)
d_op = {}
for num in num_list:
    d_op[num] = num**2
print("output dictionary: ",d_op)

"""15.merge two dictionary into one dictionary"""
d1 = {"a":1,"b":2,"c":3}
d2 = {"x":5,"y":4,"z":7}
print("d1: ",d1)
print("d2: ",d2)
for key,value in d2.items():
    d1[key] = value
    print("merged dictionary d1: ",d1)
    




