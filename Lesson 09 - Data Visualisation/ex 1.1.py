import pandas as pd
import numpy as np

table = [
    ['A', 'Noah', 90, 92],
    ['B', 'Liam', 81, 83],
    ['C', 'William', 87,85],
    ['B', 'Benjamin.', 82,80],
    ['A', 'Emma.', 90,94],
    ['C', 'Olivia', 50,60],
    ['A', 'Isabella', 70,71],
    ['C', 'Amelia', 84,86],
    ['B', 'Mia', 88,85],
]

df = pd.DataFrame(table,columns = ['class', 'name', 'math_score', 'eng_score'])

print(df.groupby(by='class').sum())
print(df.groupby(by='class').mean())
print(type(df.corr().iloc[0,1]))
#print(df.corr())
print(df.corr().iloc[0,1]) #相關係數為0.963701,數學對數學以及英文對英文的相關係數必為1