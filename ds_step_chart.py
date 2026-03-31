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

# Remove missing values
df = df.dropna()

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

# Sort values (important for step chart)
df = df.sort_values(by='B', ascending=True)

# ==============================
# STEP 5: STEP (STAIR) CHART
# ==============================
plt.figure(figsize=(10,6))

plt.step(df['A'].astype(str), df['B'], where='mid')

plt.title("Step (Stair) Chart")
plt.xlabel("A")
plt.ylabel("B")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()