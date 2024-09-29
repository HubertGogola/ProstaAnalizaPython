""""
import pandas as pd

people_data = [
    ['James','UK',30000,29],
    ['Adam','Germany',50000,33],
    ['Eva','UK',47000,29],
    ['John','Germany',60000,45],
    ['Marie','France',37000,29]
]

people_data_headers=['name','country','salary','age']

df=pd.DataFrame(people_data, columns=people_data_headers)

result= df.groupby(['country','name'])['salary'].count()

print(result)

"""