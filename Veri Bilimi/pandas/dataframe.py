import pandas as pd 

# DataFrame sayesinde verileri kolonlar haline getirebiliyoruz. 
data = [["Emre",70],["Ali",80],["Ahmet",50],["Yakup",100]]
df = pd.DataFrame(data, columns = ["Ad","Not"], index = [1,2,3,4], dtype=float) #eğer bu şekilde yazılmazsa index ve kolon sırasına göre olan yazım yapılmalı
df = pd.DataFrame(data, [1,2,3,4],["Ad","Not"]) #bu şekilde
print(df)

# dictionary ile kullanım
dictionary = {"İsim": ["Ahmet","Emre","Ali","Ayşe"],"Not":[80,60,40,70]}
df = pd.DataFrame(dictionary)
print(df)

# dictionary list
dict_list = [
                {"Name":"Ali","Grade":60},
                {"Name":"Ahmet","Grade":20},
                {"Name":"Ayşe","Grade":90},
                {"Name":"Emre","Grade":80},
            ]
df = pd.DataFrame(dict_list)
print(df)


s1 = pd.Series([3,7,4,0])
s2 = pd.Series([4,2,9,5])

data = dict(apples = s1, oranges = s2)

df = pd.DataFrame(data)
print(df)