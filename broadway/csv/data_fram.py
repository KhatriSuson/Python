# import pandas as pd 
# data = {'name':['Tara','Shyam','Gita'],
#         'age':[34,23,44],
#         'add':['ktm','patan','bktpur']}
# df = pd.DataFrame(data)
# df.to_csv('datafram.csv')
# read = pd.read_csv('datafram.csv', usecols = ['name','age','add'])
# print(read)
# print(df)

import pandas as pd 
data1 = {'name':['Tara','Shyam','Gita'],
        'age':[34,23,44],
        'add':['ktm','patan','bktpur']}


data2 = {'name':['Tara','Shyam','Gita'],
        'age':[34,23,44],
        'add':['ktm','patan','bktpur']}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df = pd.concat([df1, df2])
print(df)