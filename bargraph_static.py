import matplotlib.pyplot as plt
categories = ['January', 'February', 'March', 'April', 'May']
values = [150, 230, 180, 210, 250]
colors = ['skyblue', 'orange', 'lightgreen', 'pink', 'purple']
plt.figure(figsize=(8, 5))
plt.bar(categories, values, color=colors, edgecolor='black')
plt.xlabel("Months")
plt.ylabel("Sales Units")
plt.title("Monthly Sales Data")
plt.show()