import pandas as pd

dt = pd.read_csv("imdb.csv", sep=",")
result = dt
result = dt.columns #sütun isimlerini yazdır.
result = dt.head(10) #ilk 10 kaydı yazdır.
result = dt.tail(10) #son 10 kaydı yazdır.
result = dt[["Series_Title","Released_Year"]].head() #Series_Title ve Released_Year sütunlarının ilk 5 kaydını yazdır.
result = dt[["Series_Title","Released_Year"]].tail(7) # Series_Title ve Released_Year sütunlarının son 7 kaydını yazdır.
result = dt[5:][["Series_Title","Released_Year"]].head() #Series_Title ve Released_Year sütunlarının ikinci 5 kaydını yazdır.
sekizuzeri = dt[dt["IMDB_Rating"] >= 8.0][["Series_Title","IMDB_Rating"]].head(50) #rating'i 8 ve üzeri olan filmeleri isimleriyle yazdır.
result = sekizuzeri.sort_values("IMDB_Rating", ascending=True) #ratingler düşükten yükseğe sıralansın.

result = dt[(dt["Released_Year"] >= "1999") & (dt["Released_Year"] <= "2010")][["Series_Title","Released_Year"]] #1999 ve 2010 yılları arasında çıkan filmleri isim ve tarihleriyle yazdır.
result = len(dt.index) #toplamda kaç adet satır var yazdır.

print(result)