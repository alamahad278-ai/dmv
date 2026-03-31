import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# STEP 1: LOAD DATA
# ==============================
df = pd.read_csv("datasett.csv")

# Clean column names
df.columns = df.columns.str.strip()

print("=== DATA PREVIEW ===")
print(df.head())

# ==============================
# STEP 2: CHECK MISSING VALUES
# ==============================
print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

# Remove missing values (important for pie chart)
df = df.dropna(subset=['B'])

# ==============================
# STEP 3: OUTLIER DETECTION (IQR)
# ==============================
print("\n=== OUTLIER DETECTION ===")

Q1 = df['B'].quantile(0.25)
Q3 = df['B'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df['B'] < lower) | (df['B'] > upper)]

print("\nOutliers in B:")
print(outliers)

# ==============================
# STEP 4: PREPARE DATA
# ==============================

# Sort and take top 5 (best for pie chart)
df = df.sort_values(by='B', ascending=False).head(5)

# ==============================
# STEP 5: PIE CHART
# ==============================
plt.figure(figsize=(6,6))

plt.pie(df['B'], labels=df['A'], autopct='%1.1f%%')

plt.title("Pie Chart (Top 5 Values)")

plt.show()