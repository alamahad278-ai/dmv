import matplotlib.pyplot as plt
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78]
fig, ax = plt.subplots()
ax.scatter(x, y, color='blue', marker='o')
ax.set_xlabel("X-Axis (Independent Variable)")
ax.set_ylabel("Y-Axis (Dependent Variable)")
ax.set_title("Static Scatter Plot")
plt.show()