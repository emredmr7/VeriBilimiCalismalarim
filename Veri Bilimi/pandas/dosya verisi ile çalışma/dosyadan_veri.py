import pandas as pd

df = pd.read_csv("Kitap2.csv") #csv formatlı dosyalar için
# df = pd.read_json("belge.json") # json formatlı dosyalar için

print(df.head())