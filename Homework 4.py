# 1.
# a = input("Enter word: ")
# print(a.encode())
# 2.
# word = input("Enter a string: ")
# word = word.strip()
# word = word.lower()
# word = word.replace("python", "Python")
# word += "\nPython"
# print(word)
# 3.
# word = input("Enter a string: ")
# a = (len(word))//2
# print(word[:int(a)])
# 4.
# import string 
# word = input("Enter a string: ")
# is_valid = True
# for i in word:
#     if i in string.ascii_letters:
#         continue
#     elif i in string.digits:
#         continue
#     elif i == " ":
#         continue
#     else:
#         print("not correct sting")
#         is_valid = False
#         break
# if is_valid:
#     print("correct string")
# 5. 
# word = input("Enter a string: ")
# in_bytes = word.encode('utf-8')
# print(in_bytes)
# in_word = in_bytes.decode('utf-8')
# print(in_word)
