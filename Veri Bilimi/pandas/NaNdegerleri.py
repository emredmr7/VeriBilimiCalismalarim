import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data, index = ['a','c','e','f','h'], columns = ["Column1","Column2","Column3"])
df = df.reindex(['a','b','c','d','e','f','g','h'])
newColumn = [np.nan,30,np.nan,60,np.nan,10,np.nan,20]
df["Column4"] = newColumn

result = df
result = df.drop("Column1", axis = 1) # axislerde 0'lar satırları 1'ler sütunları temsil eder. burada column1'den bahsediyor.
result = df.drop(["Column1","Column2"], axis = 1)
result = df.drop("a", axis = 0)
result = df.drop(["a","b","h"], axis = 0)

result = df.isnull() #boş olan alanları gösterir.
result = df.notnull() #dolu alanları gösterir.
result = df.isnull().sum() #sütunlarda kaç adet boş değer olduğunu gösterir 
result = df["Column4"].isnull().sum() #4.sütunda kaç adet boş değer olduğunu gösterir.
result = df[df["Column1"].isnull()]["Column1"]

result = df.dropna() #dropna NaN değerlerini siler, satıra göre siler
result = df.dropna(axis = 1) #sütuna göre
result = df.dropna(how = "any") #herhangi bir boş değeri bulursa siler.
result = df.dropna(how = "all")  #bir satırdaki tüm değerler NaN iste siler.
result = df.dropna(subset = ["Column1","Column2"], how = "any") #sütun 1ve2'de herhangi bi NaN değer varsa siler.
result = df.dropna(thresh = 3) #en az 3 adet veri olan satırları alır

result = df.fillna(value = "no input")
print(result)

#Boş değerleri silip yerine ortalama bir sayı yazacak bir uygulama yapalım.

def ortalama(df):
    toplam = df.sum().sum()
    adet = df.isnull().sum().sum()
    return toplam / adet

sonuc = df.fillna(value = ortalama(df))
print(sonuc)