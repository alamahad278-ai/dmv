import matplotlib.pyplot as plt
x_coords = []
y_coords = []
n = int(input("Enter the number of points to plot: "))
print("Enter the coordinates for each point:")
for i in range(n):
    x = float(input(f"Enter x value for point {i+1}: "))
    y = float(input(f"Enter y value for point {i+1}: "))
    x_coords.append(x)
    y_coords.append(y)
fig, ax = plt.subplots()
ax.scatter(x_coords, y_coords, color='red', marker='o')
ax.set_xlabel("User X-Axis")
ax.set_ylabel("User Y-Axis")
ax.set_title("User Defined Scatter Plot")
ax.grid(True)
plt.show()