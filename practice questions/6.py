# Create a dictionary with three columns: Name, CGPA and Attendance. Add data for at least four students.
#  Convert the dictionary into a Pandas DataFrame and print it.

import pandas as pd
student_detail ={

      "name":['abhishek','akash','vijay','parveen'],
      'CGPA':[7.5 , 7.2,7.1,7.4],
      "Attnedence":["85%" , "90%" ,"88" ,"90"]
}

df = pd.DataFrame(student_detail)

print(df)

# output :-
# 
"""       name  CGPA Attnedence
0  abhishek   7.5        85%
1     akash   7.2        90%
2     vijay   7.1         88
3   parveen   7.4         90"""

