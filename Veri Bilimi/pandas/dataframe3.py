import pandas as pd
import numpy as np


personeller =  {
    'Çalışan'   : ['Ahmet Yılmaz','Can Ertürk','Hasan Korkmaz','Cenk Saymaz','Ali Turan','Rıza Ertürk','Mustafa Can'],
    'Departman' : ['İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları','Bilgi İşlem','Muhasebe','Bilgi İşlem'],
    'Yaş'       : [30,25,45,50,23,34,42],
    'Semt'      : ['Kadıköy','Tuzla','Maltepe','Tuzla','Kadıköy','Tuzla','Maltepe'],
    'Maaş'      : [5000,3000,4000,3500,2750,6500,4500]
}

df = pd.DataFrame(personeller)
result = df
result = df["Maaş"].sum()
result = df.groupby("Departman").groups
result = df.groupby(["Departman","Semt"]).groups

for name, group in df.groupby("Semt"):
    print(name)
    print(group)

result = df.groupby("Semt")["Maaş"].mean()
result = df.groupby("Semt")["Çalışan"].count() #semte göre kaç adet çalışan olduğunu verir.
result = df.groupby("Departman")["Maaş"].max()["Muhasebe"]
result = df.groupby("Departman").agg(np.mean)
print(result)
