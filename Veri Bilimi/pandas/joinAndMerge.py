import pandas as pd

customers =  {

    'CustomerId'    : [1,2,3],
    'FirstName'     : ['Ali','Veli','Ayşe'],
    'LastName'      : ['Demir','Kılıç','Çelik']
}

orders = {
    'OrderId'       : [10,11,12],
    'CustomerId'    : [1,2,6],
    'OrderDate'     : ['2021-01-01','2021-02-02','2021-03-03']
}

df_customers = pd.DataFrame(customers, columns = ['CustomerId','FirstName','LastName'])
df_orders = pd.DataFrame(orders, columns = ['OrderId','CustomerId','OrderDate'])

print(df_customers)
print(df_orders)

result = pd.merge(df_customers,df_orders, how="inner") #CustomerId'ye göre iki tabloyu birlikte verir. 
result = pd.merge(df_customers,df_orders, how="left") #customers'a göre order ve customer tablosunu birlikte verir. 

print(result)

customerA =  {

    'CustomerId'    : [1,2,3],
    'FirstName'     : ['Ali','Veli','Ayşe'],
    'LastName'      : ['Demir','Kılıç','Çelik']
}
customerB =  {

    'CustomerId'    : [4,5,6],
    'FirstName'     : ['Emre','Şahin','Harun'],
    'LastName'      : ['Demir','Çelik','Sinanoğlu']
}

df_customerA = pd.DataFrame(customerA, columns = ['CustomerId','FirstName','LastName'])
df_customerB = pd.DataFrame(customerB, columns = ['CustomerId','FirstName','LastName'])

sonuc = pd.concat([df_customerA,df_customerB], axis = 1)
print(sonuc)