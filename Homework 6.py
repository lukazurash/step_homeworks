y_dict = {
  "students": [
    {"id": 20, "name": "Giorgi", "age": 25},
    {"id": 25, "name": "Giorgi", "age": 23},
    {"id": 56, "name": "Nika", "age": 25},
    {"id": 100, "name": "Nika", "age": 22},
    {"id": 1232, "name": "Dato", "age": 22},
    {"id": 846723, "name": "Archili", "age": 32},
    {"id": 6751, "name": "Ana", "age": 20}
  ],
  "subjects": [
    {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "56": "B", "100": "A", "1232": "C", "846723": "A", "6751": "F"}},
    {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "56": "B", "100": "A", "1232": "C", "846723": "B", "6751": "A"}},
    {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "56": "A", "100": "A", "1232": "B", "846723": "A", "6751": "A"}},
    {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "56": "B", "100": "A", "1232": "A", "846723": "A", "6751": "A"}},
    {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "56": "B", "100": "A", "1232": "A", "846723": "A", "6751": "A"}},
  ]
}
stud_ids = [str(student["id"]) for student in y_dict["students"]]
print("Student IDs: " + ", ".join(stud_ids))
while True:
    in_id = int(input("Enter Student ID: "))
    is_there = False
    for student in y_dict.get("students"):
        stud_name = student["name"]
        stud_id = student["id"]
        stud_age = student["age"]
        if in_id == stud_id:
            print(f'Student Information:\nID: {stud_id}, Name: {stud_name}, Age: {stud_age}')
            print("="*30)
            is_there = True
            break
    if is_there:
        break  
    else:
        print("Please choose correct student ID.")
for grade in y_dict["subjects"]:
    sub_name = grade['name']
    sub_grade = grade['grades']
    str_in_id = str(in_id)
    if str_in_id in sub_grade:
        valuess = sub_grade[str_in_id]
    print(f'subject: {sub_name}, grade: {valuess} ')
    print("-"*30)

         
    