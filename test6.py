# def multiply(a, b):
#     result = 0
#     while b > 0:
#         if b & 1:
#             result = result ^ a
#         a <<= 1
#         b >>= 1
#         print(a,"   ",b)
#     print(result)
#     return result
# multiply(6,5)

# import random
# import math
# print(math.floor(3.7))
# print(round(2.3445566,5))
# print(random.uniform(3,44))
# my_dict = {'a': 1, 'b': 2, 'c': 3}

# # Using get to retrieve the value of an existing key
# value_a = my_dict.get('a')
# print(value_a)  # Output: 1

# # Using get to retrieve the value of a non-existing key
# value_d = my_dict.get('d')
# print(value_d)  # Output: None

# # Using get with a default value for a non-existing key
# value_d_default = my_dict.get('d', 0)
# print(my_dict)  # Output: 0

# d={"one":1,'abc':2}
# keys=list(d.keys())
# keys.sort()
# print(keys)
# for key in keys:
#     print(d[key])
# a=200000000000
# b=200000000000
# print(id(a))

# print(id(b))
# print(id(200000000000))
def unique(strs):
    s=set(strs)
    print(s)
unique("vfregfhncuvrgryugyugreib")