



# Q1. Create a file “people.txt” with the following data: Age agegroup height status yearsmarried 21 adult 6.0 single -1 2 child 3 married 0 18 adult 5.7 married 20 
# 221 elderly 5 widowed 2 34 child -7 married 3 i) Read the data from the file “people.txt”. ii) Create a ruleset E that contain rules to check for the following
# conditions: 1. The age should be in the range 0-150. 2. The age should be greater than yearsmarried. 3. The status should be married or single or widowed. 4. If 
# age is less than 18 the agegroup should be child, if age is between 18 and 65 the agegroup should be adult, if age is more than 65 the agegroup should be
# elderly. iii) Check whether ruleset E is violated by the data in the file people.txt. iv) Summarize the results obtained in part (iii) v) Visualize the results obtained in 
# part (iii)
In [1]:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

In [2]:data = pd.read_csv("people.txt",sep=",") 
data

Out[2]: Age agegroup height status years married

0 21 adult 6.0 single -1
1 2 child 3.0 married 0
2 18 adult 5.7 married 20
3 221 elderly 5.0 widowed 2

In [3]:def ruleset(data):
data['Rule1'] = data['Age'].apply(lambda x: x in range(0, 150))
data['Rule2'] = data.apply(lambda x: x.Age > x.yearsmarried, axis=1)
data['Rule3'] = data['status'].apply(lambda x: x in {'married', 'single', 'widowed'}) 
data['Rule4'] = data.apply(lambda x: (x.Age < 18 and x.agegroup == 'child') or
(18 <= x.Age <= 65 and x.agegroup == 'adult') or
(x.Age > 65 and x.agegroup == 'elderly'), axis=1)
    
In [4]:ruleset(data)
data

Out[4]: Age agegroup height status yearsmarried Rule1 Rule2 Rule3 Rule4
0 21 adult 6.0 single -1 True True True True
1 2 child 3.0 married 0 True True True True
2 18 adult 5.7 married 20 True False True True
3 221 elderly 5.0 widowed 2 False True True True
4 34 child -7.0 married 3 True True True False
In [5]: summary = data.loc[:, 'Rule1':'Rule4'].replace({True:1, False:0})
summary
Out[5]: Rule1 Rule2 Rule3 Rule4
0 1 1 1 1
1 1 1 1 1
2 1 0 1 1
3 0 1 1 1
4 1 1 1 0
In [6]: summary.plot(kind='bar') 
plt.show()
