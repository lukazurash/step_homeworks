import os,csv

path = 'files'
file_name = 'data3.csv'

os.makedirs(path, exist_ok=True)
file_name = os.path.join(path, file_name)
data = [
  {'name': 'Dato', 'age': 25, 'phone': "555 80 70 50"},
  {'name': 'Nika', 'age': 23, 'phone': "595 15 18 21"},
  {'name': 'Koba', 'age': 27, 'phone': "557 98 97 96"},
  {'name': 'Lika', 'age': 22, 'phone': "599 90 95 00"},
]
 
csv.register_dialect('my_dialect', delimiter='&', quoting=csv.QUOTE_STRINGS)

with open(file_name, 'w', encoding='utf-8', newline="") as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys(), dialect='my_dialect')
    writer.writeheader()
    writer.writerows(data)

    
    
    writer.writerow({'name': 'Elene', 'age': 20, 'phone': "599 81 72 53"})






import os,csv

path = 'files'
file_name = 'data3.csv'

os.makedirs(path, exist_ok=True)
file_name = os.path.join(path, file_name)


with open(file_name, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, dialect='my_dialect')

    print(reader)

    w1 = 10
    w2 = 10
    lines = 36
    counter = 0
    print('='*lines)
    for r in reader:
        if counter == 0:
            head = tuple(r.keys())
            print(f'  {head[0]:<{w1}}{head[1]:<{w2}}{head[2]}')
            print('='*lines)
            counter += 1
            
        print(f'  {r['name']:<{w1}}{int(r['age']):<{w2}}{r['phone']}')
        print('-'*lines)