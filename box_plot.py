import matplotlib.pyplot as plt

# Dataset
weights = [25, 28, 29, 30, 34, 35, 35, 37, 38]

# Create boxplot
plt.boxplot(weights)

# Labels and title
plt.xlabel("Weights (grams)")
plt.title("Box plot of box weights")

# Show plot
plt.show()