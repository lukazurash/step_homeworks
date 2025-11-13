# 1)
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __add__(self, z):
#         return Vector(self.x + z.x, self.y + z.y)
#     def __str__(self):
#         return f"({self.x}, {self.y})"
# v1 = Vector(2, 3)
# v2 = Vector(3, 4)
# v3 = v1 + v2
# print(v3)
# 2)
# class Book():
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#     def __eq__(self, other):
#         return self.title == other.title and self.author == other.author
# book1 = Book('1984', 'George Orwell')
# book2 = Book('1984', 'George Orwell')
# book3 = Book('Brave New World', 'Aldous Huxley')
# print(book1 == book2)  
# print(book1 == book3)  
# 3)
# class Car:
#     def __new__(cls, *args, **kwargs):
#         instance = super().__new__(cls)
#         return instance
#     def __init__(self, brand, model, year):
#          self.__brand = brand
#          self.__model = model
#          self.__year = year
#     @property
#     def brand(self):
#         return self.__brand
#     @brand.setter
#     def brand(self, new_brand):
#         if not isinstance(new_brand, str):
#             raise TypeError("Brand must be a string.")
#         if new_brand.strip() == "":
#             raise ValueError("Brand cannot be empty.")
#         self.__brand = new_brand.strip()
#     @property
#     def model(self):
#         return self.__model
#     @model.setter
#     def model(self, new_model):
#         if not isinstance(new_model, str):
#             raise TypeError("model must be a string.")
#         if new_model.strip() == "":
#             raise ValueError("model cannot be empty.")
#         self.__model = new_model.strip()
#     @property
#     def year(self):
#         return self.__year
#     @year.setter
#     def year(self, new_year):
#         if not isinstance(new_year, int):
#             raise TypeError("year must be an int")
#         if new_year < 1886 or new_year > 2025:
#             raise ValueError("year must be 1886 or later and less than or equal to 2025")
#         self.__year = new_year
        



