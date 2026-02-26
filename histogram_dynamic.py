import matplotlib.pyplot as plt
data = []
n = int(input("Enter the total number of data points: "))
print("Enter the values:")
for i in range(n):
    val = int(input(f"Value {i+1}: "))
    data.append(val)
b = int(input("Enter number of bins (e.g., 5 or 10): "))
fig, ax = plt.subplots()
ax.hist(data, bins=b, color='lightgreen', edgecolor='black')
ax.set_xlabel("Value Ranges")
ax.set_ylabel("Frequency")
ax.set_title("User Defined Histogram")
plt.show()