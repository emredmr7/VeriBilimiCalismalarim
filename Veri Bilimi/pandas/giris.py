import pandas as pd
import numpy as np

numbers = [1,2,3,4]
letters = ["a","b","c","d"]
dict = {'a':10,'b':20,'c':30,'d':40}
random_numbers = np.random.randint(10,100,6) # numpy üzerinden 10-100 arasında 6 adet rastgele sayı ürettik

# pandas_serileri = pd.Series(numbers) # solda index numarası, sağda liste elemanları şeklinde çıktı verir.
# pandas_serileri = pd.Series(5,[0,1,2,3])# 5 değerine [] içindeki index değerlerini atadık.
# pandas_serileri = pd.Series(numbers, ["k","l","m","n"])# number içindeki değerlere [] içindeki değerleri index olarak atar.
# pandas_serileri = pd.Series(dict)
# pandas_serileri = pd.Series(random_numbers)

pandas_serileri = pd.Series([20,30,40,50],['a','b','c','d'])
# result = pandas_serileri[0] #birinci elemanı verir
# result = pandas_serileri[-1] #sonuncu elemanı verir
# result = pandas_serileri[:2] # ilk iki elemanı verir
result = pandas_serileri[-2:] # son iki elemanı verir
# result = pandas_serileri['a'] # a keyine denk gelen değeri verir.
# result = pandas_serileri.ndim # kaç boyutlu olduğnu gösterir.
# result = pandas_serileri+50 # tüm elemanlara 50 ekler

#print(pandas_serileri)
print(result)