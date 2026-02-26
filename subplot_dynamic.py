import matplotlib.pyplot as plt
n1 = int(input("Enter number of points for Plot 1: "))
x1, y1 = [], []
print("Enter data for Plot 1:")
for i in range(n1):
    x1.append(float(input(f"  x[{i+1}]: ")))
    y1.append(float(input(f"  y[{i+1}]: ")))
n2 = int(input("Enter number of points for Plot 2: "))
x2, y2 = [], []
print("Enter data for Plot 2:")
for i in range(n2):
    x2.append(float(input(f"  x[{i+1}]: ")))
    y2.append(float(input(f"  y[{i+1}]: ")))
fig, ax = plt.subplots(1, 2, figsize=(12, 5))
ax[0].plot(x1, y1, marker='o', color='blue', linestyle='-')
ax[0].set_title("User Plot 1 (Line)")
ax[0].set_xlabel("X Axis")
ax[0].set_ylabel("Y Axis")
ax[0].grid(True)
ax[1].scatter(x2, y2, color='red', marker='x')
ax[1].set_title("User Plot 2 (Scatter)")
ax[1].set_xlabel("X Axis")
ax[1].set_ylabel("Y Axis")
ax[1].grid(True)
plt.tight_layout()
plt.show()