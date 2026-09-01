import pandas as pd


data = {

      "Name":["Aman",'Riyan',"shila"],
      "CGPA":[5.2,3.4,6.4],
      'projects':[3,4,5]
}

df=pd.DataFrame(data)

print(df)

# out put:-
"""
    Name  CGPA  projects
0   Aman   5.2         3
1  Riyan   3.4         4
2  shila   6.4         5
"""

"""data frame is conter of python to store data """