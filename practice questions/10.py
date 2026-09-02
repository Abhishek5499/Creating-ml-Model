# Create a dictionary containing Name, CGPA, Attendance, Projects and Placed for at least five students. Convert it to a DataFrame. Then print the complete DataFrame and also print type(df). 
# In one sentence, explain why a DataFrame is useful before machine learning.

import pandas as pd
s_details = {

      'Names':('Abhi','Ganesh','vignesh','livo','dk'),
      'CGPA':(5,6,3,7,8),
      'Attnedence%':('50','80','59','58','86'),
      'projects':(3,4,2,5,6)
}

df = pd.DataFrame(s_details)

print(df)

# out put:

'''     Names  CGPA Attnedence%  projects
0     Abhi     5          50         3
1   Ganesh     6          80         4
2  vignesh     3          59         2
3     livo     7          58         5
4       dk     8          86         6'''
