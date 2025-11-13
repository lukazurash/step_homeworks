# 1. დაწერეთ პითონის ფუნქცია რომელიც კონტექსტის მენეჯერის გამოყენებით პარამეტრად მიიღებს ფაილის საქაღალდის მისამართს, ფაილის სახელს და შემქნის მას.

# 2. დაწერეთ პითონის ფუნქცია რომელიც წაიკითხავს პარამეტრად მიღებული ფაილის კონტენტს.

# 3. დაწერეთ პითონის ფუნქცია რომელიც პარამეტრად მიიღებს ლექსიკონს (dict) და დაამატებს ფაილის კონტენტს.

# [
#   {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
#   {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
# ]

# ბოლოში უნდა ჩაემატოს მხოლოდ ორი ლექსიკონი და არა სია.

# 4. დაწერეთ პითონის ფუნქცია, რომელიც გაანახლებს ფაილში არსებულ კონტენტს.
import os, json
chess_players = [
  {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
  {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
  {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
  {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
  {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
  {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
  {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
  {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
  {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
]
new_players = [
  {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
  {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
]

def open_file(path_name, file_name, data):
    os.makedirs(path_name, exist_ok=True)
    file_path = os.path.join(path_name, file_name)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)


def read_file(f_path):
    with open(f_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data
open_file("files", "data.json", chess_players)
data = read_file("files/data.json")
print(data)


def file_append(f_path, new_players):
    data = read_file(f_path)
    for d in new_players:
        data.append(d)
    with open(f_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)


def update_data(f_path, new_players):
    if os.path.exists(f_path):
        with open(f_path, 'w', encoding='utf-8') as f:
            json.dump(new_players, f, indent=2, ensure_ascii=False)
        print("file updated")
    else:
        print("file not found")