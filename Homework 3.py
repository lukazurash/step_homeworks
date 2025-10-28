# 1.
# a = int(input("Enter ur number: "))
# b = 0
# for i in range(1, a+1):
#     b+=i
# print(b)
# 2.
# a = int(input("enter ur number: "))
# print(a)
# while a>1:
#     a-=1
#     print(a)
# 3. დაწერეთ პითონის პროგრამა თამაშისთვის, რომელიც მუდმივად სთხოვს მომხმარებელს გამოიცნოს წინასწარ განსაზღვრული რიცხვი.
#  როდესაც მომხმარებელი გამოიცნობს სწორ რიცხვს, დაასრულებს პროგრამა მუშაობას.
# from random import randint 
# randomnum = randint(1, 100)
# a = 0
# while a!=randomnum:
#     a = int(input("Guess the Number: "))
#     if a == randomnum:
#         print("U Guessed it right")
#         break
#     elif a > randomnum:
#         print("ur guess is higher thn randomnum")
#     else:
#         print("ur guess is less thn randomnum")
# print("finished")
# 4.  დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მუდმივად რიცხვებს. შექმენით საწყისი ცვლადი total_sum = 0,
#  შეამოწმეთ რიცხვი თუ დადებითია, მხოლოდ მაშინ დაუმატეთ total_sum ცვლადს. ეს პროცესი გაგრძელდეს იქამდე სანამ მომხმარებელი არ შეიყვანს 
# 'sum' ტექსტს, რის შემდეგაც დაიბეჭდება შეყვანილი დადებითი რიცხვების ჯამი.
# total_sum = 0
# while True:
#     a = input("enter the number or sum: ")
#     if a == "sum":
#         print(total_sum)
#         break
#     if a.isdigit():
#       total_sum+=int(a)
#     else:
#        print("please enter a valid number or 'sum' ")
    

