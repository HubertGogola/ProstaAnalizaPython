import pandas as pd

people_data = [
    ['James','UK',30000,29],
    ['Adam','Germany',50000,33],
    ['Eva','UK',47000,29],
    ['John','Germany',60000,45],
    ['Marie','France',37000,29]
]


naglowki=['names','country','salary','age']

df=pd.DataFrame(people_data, columns=naglowki)

result= df.loc[df['age'] < 30]

names=['John','James']

print(result)