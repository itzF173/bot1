from sklearn.linear_model import LinearRegression
#import numpy as np

model1 = LinearRegression()

rots = [[1],[2],[3],[4]]

ves = [100,90,80,60]

x = model1.fit(rots,ves)
y = model1.predict([[5]])
print(y)

data = []

row = {"size":2,"tolsh":0.2,"name":"apple"}
data.append(row)
row = {"size":5,"tolsh":0.5,"name":"orange"}
data.append(row)

def fruits(color, size):
    if(size < 5):
        return "apple"
    elif (color == "red"):
        return "apple"
    else:
        return "orange"
print(fruits("orange", 6))

for i in data:
    print(f"Размер - {i["size"]}, Тол")