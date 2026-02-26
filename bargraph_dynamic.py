import matplotlib.pyplot as plt
values = []
n = int(input("Enter the number of bars: "))
for i in range(n):
    val = float(input(f"Enter numerical value for bar {i+1}: "))
    values.append(val)
labels = [str(i+1) for i in range(n)]
fig, ax = plt.subplots()
ax.bar(labels, values, color='skyblue', edgecolor='black')
ax.set_xlabel("Category Number")
ax.set_ylabel("Values")
ax.set_title("User Defined Numerical Data")
plt.show()