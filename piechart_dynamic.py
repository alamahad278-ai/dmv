import matplotlib.pyplot as plt
labels = []
values = []
n = int(input("Enter the number of categories: "))
for i in range(n):
    label = input(f"Enter name for category {i+1}: ")
    val = float(input(f"Enter value for {label}: "))
    labels.append(label)
    values.append(val)
fig, ax = plt.subplots()
ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
ax.set_title("User Defined Data Distribution")
ax.axis('equal')
plt.show()