import os,csv
from operator import itemgetter
path = 'files'
file_name = 'students.csv'

os.makedirs(path, exist_ok=True)
file_name = os.path.join(path, file_name)
students = [
    {'id': 1, 'name': 'Anna', 'age': 16, 'grade': '10th', 'subject_name': 'Math', 'mark': 10},
    {'id': 2, 'name': 'Luka', 'age': 17, 'grade': '11th', 'subject_name': 'Physics', 'mark': 2},
    {'id': 3, 'name': 'Nino', 'age': 15, 'grade': '9th', 'subject_name': 'English', 'mark': 10},
    {'id': 4, 'name': 'Giorgi', 'age': 18, 'grade': '12th', 'subject_name': 'Chemistry', 'mark': 9},
    {'id': 5, 'name': 'Mari', 'age': 16, 'grade': '10th', 'subject_name': 'History', 'mark': 8}
]
headers = ['id', 'name', 'age', 'grade', 'subject_name', 'mark']
with open(file_name, 'w', encoding='utf-8') as c:
    writer = csv.DictWriter(c, fieldnames=students[0].keys())
    writer.writeheader() 
    writer.writerows(students)
def add_student():
    stud_data = []
    with open(file_name, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        stud_id = [int(row['id']) for row in reader]
    while True:
        a = input("Please add a new student id: ")
        if not a.isdigit():
            print("id must be a number.")
            continue
        a = int(a)
        if a in stud_id:
            print("This id is already used, choose another one")
        else:
            stud_data.append(a)
            break
    for i in headers[1:]:
        a = input(f'Please Add a new student insert {i}: ')
        if i == 'age' or i == 'mark':
            stud_data.append(int(a))
        else:
            stud_data.append(a)
    new_student = dict(zip(headers, stud_data))
    with open(file_name, 'a', encoding='utf-8', newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writerow(new_student)

    def get_id(row):
        return int(row['id'])
    with open(file_name, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    data.sort(key=get_id)
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
    print(f'student {new_student['name']} added')
# while True:
#     add_student()
#     add_another = input("\nif u want to add another student type yes else type no:  ").strip().lower()
#     if add_another != 'yes':
#         print("Exiting")
#         break
def stud_infos():
    with open(file_name, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    while True:
        in_id = input("Please enter the id of the student or just type 'all' to see all students informations: ")
        is_there = False
        if in_id == 'all':
            print("\n All Students:\n")
            print(f"{'ID':<5} {'Name':<10} {'Age':<5} {'Grade':<8} {'Subject':<12} {'Mark':<5}")
            print("-" * 50)
            for stud in data:
                print(f"{stud['id']:<5} {stud['name']:<10} {stud['age']:<5} {stud['grade']:<8} {stud['subject_name']:<12} {stud['mark']:<5}")
            print("-" * 50)
            print(f"Total students: {len(data)}\n")
            break 
        for stud in data:
            stud_id = stud['id']
            stud_name = stud['name']
            stud_age = stud['age']
            stud_grade = stud['grade']
            stud_sub = stud['subject_name']
            stud_mark = stud['mark']
            if in_id == stud_id:
                print(f'Student Information:\nID: {stud_id}, Name: {stud_name}, Age: {stud_age}, grade: {stud_grade}, subject: {stud_sub}, mark: {stud_mark}')
                is_there = True
                break
        if is_there:
            break  
        else:
                print("Please choose correct student ID.")
# stud_infos()
def avarage_score():
    with open(file_name, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
        counter = 0
        stud_mark = []
        for stud in data:
            counter+=1
            stud_mark.append(int(stud['mark']))

        print(sum(stud_mark)/counter)
# avarage_score()
def change_mark():
    with open(file_name, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    
    in_id = input("please enter student id: ")
    in_sub = input("please enter subject: ").capitalize()
    found = False
    for stud in data:
        if stud['id'] == in_id and stud['subject_name'] == in_sub:
            mark_change = input("Please enter new mark: ")
            stud['mark'] = mark_change
            found = True
            break
    if not found:
        print("there isnt a student with this id or subject")
    else:
        print("mark updated")
    with open(file_name, 'w', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
change_mark()





