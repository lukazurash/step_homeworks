# 1.
# def append(a):
#     int_list.append(a)
#     print(int_list)



# int_list = [10,20,30,40]
# append(2)
# 2.
# def summ(l):
#     a = sum(l)
#     print(a)


# summ([100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10])
# 3.
# def gl():
#     gl_star = "local"
#     print(gl_star)


# gl_str = "Global"
# gl()

# print(gl_str)
# 4.
# def numbers_sum(number):
#     number = str(number)
#     if len(number) == 1:
#         return int(number)
#     return int(number[0]) + numbers_sum(number[1:])
# 5.
# print(numbers_sum(100000000000000000000001))
# def reverse(strr):
#     if len(strr) == 1:
#         return strr
#     return strr[-1]+reverse(strr[:-1])
# print(reverse("hello"))
# 6.
def flatten(arg):
    for item in arg:
        if isinstance(item, (list,tuple,set,frozenset)):
            yield from flatten(item)
        elif isinstance(item, (dict)):
            yield from flatten(item.values())
        else:
            yield item
arr = [1,2,(3,[[4,5,6],"text", 7]),{'title': 'the wolf', 'pages':156}]
ar = flatten(arr)
print(*ar)
