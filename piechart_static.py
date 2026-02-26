import matplotlib.pyplot as plt
labels = ['A', 'B', 'C', 'D']
values = [400, 300, 150, 250]
colors = ['gold', 'lightskyblue', 'lightcoral', 'lightgreen']
fig, ax = plt.subplots()
ax.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax.set_title("Sales Distribution by Category")
ax.axis('equal')
plt.show()