
import pandas as pd

people_data=[
    ['James', 'Smith', 3000,29],
    ['Adam', 'Black',50000, 33],
    ['Eva', 'Jameson', 47000, 45],
    ['John','Geere',31000,29],
    ['Roger','White',54000,35],
    ['Philip','Red',42000,41]
]

df1 = pd.DataFrame(people_data) #tworzenie dataframa

#print(df1.head()) #pierwsze 5 rzędów bez .head cala lista

people_date_headers=['name','surname','salary','age'] #nazywanie tytulow kolumn

df2=pd.DataFrame(people_data, columns=people_date_headers)

print(df2.head())

print(df2.info())

print(df2.describe())

print(df2.shape)

print(df2.columns)

print(df2.index)

print(df2.values)
