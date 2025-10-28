# 1.
# arr1 = [1, 2, 3] 
# arr2 = ['a', 'b', 'c']  
# arr3 = list(zip(arr1,arr2))
# print(arr3)
# 2.
# from functools import reduce
# a = [1, 2, 3,{'s': 's'}, 4, 5, 6]
# try: 
#     pr = reduce(lambda x,y:x*y,a)
#     print(pr)
# except TypeError as e:
#     print("Type Errorrr!!!")
# except Exception as ex:
#     print(ex)
# 3.
# a =[1, 2, 3, 4, 5, 6, 7]
# odd = lambda a:[x for x in a if x%2 == 1] 
# print(odd(a))
# 4.
# lst = ['hello', 'world', 'coding', 'nod']
# try:
#     ing = list(filter(lambda x: x[-3:] == 'ing', lst))
#     print(ing)
# except TypeError:
#     print("type error")
# except Exception as ex:
#     print("ERROR", ex)
# 4.1
# lst = ['hello', 'world', 'coding', 'nod']
# ing = list(filter(lambda x: x.endswith('ing'), lst))
# print(ing)


