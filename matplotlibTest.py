import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,4,8,16,32]

plt.plot(x,y, marker='o', linestyle='--', color='r')
plt.title("График")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

i = 0
while i < len(x):
    y[i] = x[i]^2