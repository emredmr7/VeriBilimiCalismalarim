import numpy as np

numbers = np.array([0,5,10,15,20,25,50,75])

result = numbers[5] #5.indexdeki elemanı alır
result = numbers[-1] #sondaki elemanı alır
result = numbers[:3] #3.indexten öncesini alır.
result = numbers[3:] #3.indexten sonrasını alır.
result = numbers[::] #bütün listeyi alır.
result = numbers[::-1] #bütün listeyi tersten teker teker yazar.
result = numbers[::-2] # bütün listeyi tersten bir atlayarak yazar.
print(result)
print("****************")

numbers2 = np.array([[0,5,10],[15,20,25],[30,35,40]])

result2 = numbers2[1] #1.indexdeki grubu alır.
result2 = numbers2[0,2] #0.indexdeki grubun 2.indexdeki elemanını alır
result2 = numbers2[:,1] #bütün grupların 1.indeksdeki elemanlarını alır.
result2 = numbers2[:,0:2] #bütün grupların 0dan 2.indekse kadar olan elemanlarını alır. 2dahil değil.
result2 = numbers2[-1,:] #sondaki grubun tüm elemanlarını alır. 
result2 = numbers2[:2,:2] #2.indekse kadar olan grupları ve 2.indekse kadar olan değerleri alır
#veya ilk iki grubu ve ilk iki değerlerini alır da diyebiliriz.
print(result2)
print("--------------------")
arr1 = np.arange(0,10) 
arr2 = arr1 #eğer bu şekilde yazarsak alttaki 20 değeri arr1'e de geçer
arr2 = arr1.copy() # bu şekilde yazarsak sadece arr2'de değişiklik yapmış oluruz.

arr2[0] = 20
print(arr1)
print(arr2)