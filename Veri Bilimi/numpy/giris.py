import numpy as np

# numpy array

dizi = np.array([1,2,3,4,5,6,7,8,9]) # tek boyutlu dizi
a = dizi.reshape(3,3) #reshape ile 9 elemanlı diziyi 3-3 şeklinde ayırdık
print(a)

dizi2 = np.array([[1,2,3],[4,5,6],[7,8,9]]) #çok boyutlu dizi
print(dizi2)

print(dizi.ndim) #ndim, dizinin kaç boyutlu olduğunu gösterir
print(dizi2.ndim)

print(dizi.shape) #shape bir dizinin kaça kaçlık bir dizi olduğunu belirtir.
print(dizi2.shape)

result = np.arange(1,10,2) #1'den 10'a kadar sayı oluşturur. Eğer 3.bir sayı girilirse kaçar kaçar sayacağını belirtir.
result = np.zeros(7) #zeros(), parantez içine yazılan sayı kadar 0 olan bir dizi yapar
result = np.ones(7)  #ones(), parantez içine yazılan sayı kadar 1 olan bir dizi yapar
result = np.linspace(0,100,5) #linspace verilen değerleri en sondaki değer kadar eşit aralıklarla böler, başlangıç bitiş sayıları dahil.
result = np.random.randint(0,10) # 0 ve 10 arasında rastgele sayı üretir.
result = np.random.rand(5) # 0 ve 1 arasında rastgele parantez içi kadar pozitif sayı üretir.
result = np.random.randn(5) # # 0 ve 1 arasında rastgele parantez içi kadar negatif ve pozitif sayı üretir.

rnd_numbers = np.random.randint(1,100,10)
result = rnd_numbers.max() #max yukarıda rastgele ürettiğimiz 10 sayı içinden en büyüğünü alır
result = rnd_numbers.min() #min yukarıda rastgele ürettiğimiz 10 sayı içinden en küçüğünü alır
result = rnd_numbers.mean() #mean yukarıda rastgele ürettiğimiz 10 sayının ortalamasını alır
result = rnd_numbers.argmax() # en büyük sayının kaçıncı index'te olduğunu gösterir.
result = rnd_numbers.argmin() # en küçük sayının kaçıncı index'te olduğunu gösterir.
print(rnd_numbers,"-",result)
