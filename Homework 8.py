# 1.
# def fibo(n):
#     a=0
#     b=1
#     arr=[]
#     for i in range(n):
#         arr.append(a)
#         a,b=b,a+b
#     return arr
# N = 10
# r = fibo(N)
# print(r)
# 2.
# def an(a,b):
#     if sorted(a)==sorted(b):
#         print("they are")
#     else:
#         print("they arent")
# an("race","care")
# 3.
# def faqt(n):
#     count = 1
#     for i in range(1, n+1):
#         count*=i
#     print(count)
# N= 4
# faqt(N)
# 4.
# def func(a,b):
#     count = 0
#     for i in a:
#         if b == i:
#             count+=1
#     print(count)


# func("luaabbkaaaa", "a")
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