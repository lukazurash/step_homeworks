# 1.
# em_list = []
# while True:
#     are = input("Enter 'a'-append, 'r'-remove or 'e'-exit: ")
#     if are == "a":
#         n = int(input("Enter a number to append: "))
#         em_list.append(n)
#         print(em_list)
#     elif are == "r":
#         if em_list:
#             n = int(input("Enter a number to remove: "))
#             if n in em_list:
#                 em_list.remove(n)
#             else:
#                 print("n is not in list")
#         else:
#             print("list is empty")
#     elif are == "e":
#         print("finished list:", em_list)
#         break
#     else:
#         print("please only use these commands: 'a', 'r', 'e'.")
# 2.
# my_list_1 = [43, '22', 12, 66, 210, ["hi"]]
# print(my_list_1.index(210))
# my_list_1[len(my_list_1)-1].append("hello")
# print(my_list_1)
# my_list_1.pop(2)
# print(my_list_1)
# my_list_2 = my_list_1.copy()
# my_list_2.clear()
# print(my_list_1, my_list_2)
# 3.
# import re
# n = "(123) 456-789"
# pattern = r"\(\d{3}\) \d{3}-\d{3}"
# matched = re.fullmatch(pattern, n)
# if matched:
#     print(n)
# else:
#     print("not matched")

