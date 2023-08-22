# import csv
# info = [['name','age','add'],
#         ['Ram','32','lalitpur'],
#         ['Sita','23','ktm'],
#         ['Gita','43','bkt']]
# file = open('list_data.csv', 'w')
# x = csv.writer(file)
# x.writerows(info)
# file.close()

# import pandas as pd 
# df = pd.read_csv('list_data.csv')
# print(df)


# import csv
# with open('list_data.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row)



import pandas as pd 
import csv
data = [{'name': 'Ram', 'age': '32', 'add': 'lalitpur'},
{'name': 'Sita', 'age': '23', 'add': 'ktm'},
{'name': 'Gita', 'age': '43', 'add': 'bkt'}]
c = ['name','age','add']

with open("data.csv", 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = c)
    writer.writeheader()
    writer.writerows(data)
df = pd.read_csv('data.csv')
print(df)