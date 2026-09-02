# Create a dictionary with Name, Marks and City for at least 4 students. Convert it into a Pandas DataFrame.
# Print the DataFrame and then print only the Name column.

import pandas as pd

d1={
    "Name":('Abhi','Ganesh','vignesh','livo'),
    'Marks':(90,50,80,70),
    'City':('Mumbai','Pune','Bangalore','Bidar')
}

a= pd.DataFrame(d1)

print(a['Name'])

