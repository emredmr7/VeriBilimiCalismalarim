import pandas as pd
import numpy as np

data = {
    'Column1' : [1,2,3,4],
    'Column2' : [10,20,30,20],
    'Column3' : ['abc','bca','cba','dba']
}

df = pd.DataFrame(data)

result = df
result = df['Column2'].value_counts() #hangi verinin kaç adet olduğunu gösterir.
result = df.sort_values('Column3') #sort_values() da parantez içine girilen parametredeki str veya int değerlerini sıralar.
result = df.sort_values('Column3', ascending=False) #tersten sıralar.

print(result)