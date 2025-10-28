# 1. კონსოლიდან შეიტანეთ ორი რიცხვი და დაბეჭდეთ ყველა არითმეტიკული ოპერაცია (მიმატება, გამოკლება, გამრავლება, ჩვეულებრივი გაყოფა, მთელზე გაყოფა, ნაშთის აღება, ახარისხება).

# 2. დაწერეთ პროგრამა რომბის ფართობის გამოსათვლელად. მომხმარებელს კლავიატურის გამოყენებით შეაქვს ორი დიაგონალის სიგრძე.

# 3. მომხმარებელის შეაქვს მეტრების რაოდენობა. დაბეჭდეთ შესაბამისი მნიშვნელობა სანტიმეტრებში, დეციმეტრებში, მილიმეტრებში, მილში.

# 4. დაწერეთ პროგრამა, რომელიც ითვლის სამკუთხედის ფართობს. მომხმარებელს კონსოლიდან შეყავს სამკუთხედის სიმაღლისა და ფუძის მნიშვნელობა.

# 5. კონსოლიდან შეიტანეთ ორნიშნა რიცხვი და დაბეჭდეთ ციფრთა ჯამი.

# a = eval(input("Please Enter First Number: "))
# b = eval(input("Please Enter Second Number: "))
# print(f'Sum = {a+b}, mult = {a*b}, gamokleba = {a-b}, chv gay = {a/b}, mt gay = {a//b}, nash = {a%b}, ax = {a**b}')
# a = eval(input("Please Enter First Number: "))
# b = eval(input("Please Enter Second Number: "))
# print(f'fartobi = {a*b/2}')
# a = int(input("Please Enter First Number: "))
# a = str(a)
# count = 0
# for i in a:
#     count += int(i)
# print(count)
# 1. შექმენით სია num_list [44, 23, 11, 8, 20, 56, 33, 55], in-ის გამოყენებით დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ შეტანილი რიცხვი არის თუ არა სიაში.

# მაგ.:
# Enter a number: 56
  
# The number in list

# #===========================

# Enter a number: 45
  
# The number not in list



# 2. დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ შეყვანილი რიცხვის ლუწობასა და კენტობას. თუ რიცხვი ლუწია გამოიტანეთ ტექსტი 'even' თუ კენტია 'odd'.

# მაგ.:

# Enter an integer: 25
  
# The number is odd

# #===========================

# Enter an integer: 36
  
# The number is even



# 3. შექმენით ორი სტრინგის ტიპის ცვლადი st1 და st2, შეადარეთ ისინი is-ის გამოყენებით, თუ ემთხვევა გამოიტანეთ ტექსტი "Same object", წინააღმდეგ შემთხვევაში "Different object"

# num_list = [44, 23, 11, 8, 20, 56, 33, 55]
# a = int(input("enter the number: "))
# if a in num_list:
#     print("yes")
# else:
#     print("no")
# a = "luka"
# b = "lukaa"
# if a is b:
#     print("yes")
# else:
#     print("no")
# a = int(input("enter the number: "))
# count = 0
# for i in range(a):
#     count+=i
# print(count)
# a = int(input("enter ur number: "))
# print(a)
# while a > 1:
#     a-=1
#     print(a)
# from random import randint as rint
# a = rint(1,100)
# b = 0

# while a!=b:
#     b = int(input("guess the number: "))
#     if b>a:
#         print("the number is less thn ur guess")
#     elif b<a:
#         print("the number is more thn ur guess")
#     else:
#         print(f"u guessed the number its {a}")
# else: 
#     print("finished")
# total_sum = 0
# while True:
#     a = input("enter the number")
#     if a =="sum":
#         print(total_sum)
#         break
#     if a.isdigit():
#         total_sum+=int(a)
#     else:
#         print("please enter number or sum")
# a ="  python is FFFFunny     "
# a = a.strip()
# a = a.lower()
# a+= "\nPython"
# if "python" in a:
#     a = a.replace("python", "Python")
# print(a)
# a = input("enter the string: ")
# print(a[:len(a)//2])
# word = input("Enter a string: ")
# a = (len(word))//2
# print(word[:int(a)])
# import string

# user_input = input("Enter a string: ")

# found_symbol = False
# for ch in user_input:
#     if ch in string.punctuation:
#         found_symbol = True
#         break

# if found_symbol:
#     print("no")
# else:
#     print("yes")
# from random import randint

# arr = []
# while True:
#     stri = input("please choose: a, r, e: ")
#     if stri == "a":
#         a = input("please enter the number to append")
#         if a.isdigit():
#             arr.append(int(a))
#         else:
#             print("please enter only numbers!.")
#     elif stri == "r":
#         r = int(input("please enter the number to remove"))
#         if r in arr:
#             arr.remove(r)
#         else:
#             print(f"This number isnt in list please choose from arr: {arr}")
#     elif stri == "e":
#         print(f'Finished List: {arr}')
#         break
#     else:
#         print("Please enter only a,r,e.")
# import re
# a = "(123) 456-789"
# pattern = r"\(\d{3}\) \d{3}-\d{3}"
# matched = re.fullmatch(pattern, a)
# if matched:
#     print(a)
# else:
#     print("no")

# n = "(123) 456-789"
# pattern = r"\(\d{3}\) \d{3}-\d{3}"
# matched = re.fullmatch(pattern, n)
# if matched:
#     print(n)
# else:
#     print("not matched")

# my_dict = {
#   "students": [
#     {"id": 20, "name": "Giorgi", "age": 25},
#     {"id": 25, "name": "Giorgi", "age": 23},
#     {"id": 56, "name": "Nika", "age": 25},
#     {"id": 100, "name": "Nika", "age": 22},
#     {"id": 1232, "name": "Dato", "age": 22},
#     {"id": 846723, "name": "Archili", "age": 32}
#   ],
#   "subjects": [
#     {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "56": "B", "100": "A", "1232": "C", "846723": "A"}},
#     {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "56": "B", "100": "A", "1232": "C", "846723": "B"}},
#     {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "56": "A", "100": "A", "1232": "B", "846723": "A"}},
#     {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "56": "B", "100": "A", "1232": "A", "846723": "A"}},
#     {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "56": "B", "100": "A", "1232": "A", "846723": "A"}},
#   ]
# }

# id_list = []
# for i in my_dict.get("students"):
#     s_id = i["id"]
#     id_list.append(s_id)
# print('studentebis ID:', ', '.join(map(str, id_list)))
# while True: 
#     in_id = int(input("Please Choose The Id: "))
#     is_there = False
#     for student in my_dict.get("students"):
#         stud_id = student["id"]
#         stud_name = student["name"]
#         stud_age = student["age"]
#         if in_id == stud_id:
#             print(f'ID: {stud_id}, Name: {stud_name}, Age: {stud_age}')  
#             is_there = True 
#             break
#     if is_there:
#         break  
#     else:
#         print("Please choose from the student ID list!")
# for subject in my_dict.get("subjects"):
#     sub_name = subject["name"]
#     sub_grade = subject["grades"]
#     str_in_id = str(in_id)
#     if str_in_id in sub_grade:
#         valuess = sub_grade[str_in_id]
#     print(f'subject: {sub_name}, grade: {valuess} ')
#     print("-"*30)
   
    
# def fibbo(n):
#     a = 0
#     b = 1
#     arr = []
#     for i in range(n):
#         arr.append(a)
#         a,b=b,a+b
#     print(arr)
# fibbo(5)
# import os, json
# path = 'files'
# file_name = 'data.json'
# os.makedirs(path, exist_ok=True)
# file_name = os.path.join(path, file_name)
# print(file_name)
# data = [
#   {'name': 'Tom', 'age': 24, 'phone': '258 693 254'},
#   {'name': 'Jane', 'age': 31, 'phone': '147 325 189'},
#   {'name': 'John', 'age': 29, 'phone': '410 189 239'},
# ]
# with open(file_name, 'w', encoding = 'utf-8') as f:
#     f.write(json.dumps(data, indent = 4)) 
# with open(file_name, 'r', encoding = 'utf-8') as f:
#     data = json.loads(f.read())
# print(data)

import os, csv

# path = 'files'
# file_name = 'data1.csv'
# os.makedirs(path, exist_ok = True)
# file_name = os.path.join(path, file_name)
# with open(file_name, 'w', encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['Name', 'Age','phone'])
#     writer.writerow(['John', 56, "558 51 03 14"])
#     writer.writerow(['Jane', 32, "558 52 01 44"])
#     writer.writerow(['Tim', 22, "558 52 01 42"])
#     writer.writerow(head)
#     writer.writerows(data)

