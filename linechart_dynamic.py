import matplotlib.pyplot as plt
n = int(input("Enter number of points: "))
x = []
y = []
print("Enter x and y values:")
for i in range(n):
    val_x = float(input(f"x[{i}]: "))
    val_y = float(input(f"y[{i}]: "))
    x.append(val_x)
    y.append(val_y)
plt.plot(x, y, marker='x', color='red')
plt.title("User Defined Line Graph")
plt.xlabel("User X")
plt.ylabel("User Y")
plt.show()