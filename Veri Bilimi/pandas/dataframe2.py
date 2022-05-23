import pandas as pd
from numpy.random import rand, randn

df = pd.DataFrame(rand(3,3), index = ["A","B","C"], columns=["Column1","Column2","Column3"])

result = df["Column1"]
result = df.loc["A"]
result = df.loc[:,"Column1"]
result = df.loc[:,["Column1","Column3"]] #1 ve 3. sütunlardaki tüm verileri verdi.
result = df.loc[:,"Column1":"Column2"] # 1den 2ye kadar tüm değerleri verdi.
result = df.loc[:,:"Column2"] #2.sütun dahil olmak üzere önceki sütünları verir.
result = df.loc["A":"B",:"Column1"] #sütun 1in a ve değerlerini verir.
result = df.iloc[2] # iloc ile indexlere göre işlem yapılır.
result = df.loc[["A","B"],["Column1","Column3"]]

df["Column4"] = pd.Series(randn(3), ["A","B","C"]) #rastgele sayılardan 4.bir sütun oluşturduk
df["Column5"] = df["Column1"] + df["Column3"]

result = df.drop("Column5", axis = 1, inplace=False) #sütun 5i listeden çıkarırız. inplace true ile kalıcı hale gelir.

print(result)
print(df)
