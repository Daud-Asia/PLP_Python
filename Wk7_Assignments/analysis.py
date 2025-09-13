# pcb_analysis.py
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------
# Task 1: Load and Explore Data
# ----------------------------
print("=== Task 1: Load and Explore the Dataset ===\n")

# Load dataset, skipping first 3 header rows
df = pd.read_csv("PCB Defects.csv", skiprows=3)

# Keep only relevant columns
df = df[["Defect", "Count"]]

# Show first few rows
print("First 5 rows of dataset:\n", df.head(), "\n")

# Show dataset info (structure, datatypes, missing values)
print("Dataset Info:")
print(df.info(), "\n")

# Check missing values
print("Missing values in each column:\n", df.isnull().sum(), "\n")

# Clean dataset (drop missing rows if any)
df = df.dropna()

# ----------------------------
# Task 2: Basic Data Analysis
# ----------------------------
print("=== Task 2: Basic Data Analysis ===\n")

# Basic statistics
print("Summary Statistics of numerical columns:\n", df.describe(), "\n")

# Calculate percentages and cumulative %
df["Percent"] = (df["Count"] / df["Count"].sum()) * 100
df = df.sort_values(by="Count", ascending=False).reset_index(drop=True)
df["CumulativePercent"] = df["Percent"].cumsum()

print("Dataset with percentages:\n", df, "\n")

# ----------------------------
# Task 3: Visualizations
# ----------------------------
print("=== Task 3: Data Visualizations ===\n")

# 1. Bar chart (Defects vs Count)
plt.figure(figsize=(7,5))
plt.bar(df["Defect"], df["Count"], color="skyblue", edgecolor="black")
plt.title("PCB Defects - Bar Chart")
plt.xlabel("Defect Type")
plt.ylabel("Count")
plt.savefig("bar_chart.png")
plt.close()

# 2. Histogram of Counts
plt.figure(figsize=(7,5))
plt.hist(df["Count"], bins=5, color="orange", edgecolor="black")
plt.title("Histogram of Defect Counts")
plt.xlabel("Count")
plt.ylabel("Frequency")
plt.savefig("histogram.png")
plt.close()

# 3. Pareto Chart (Bar + Cumulative Line)
fig, ax1 = plt.subplots(figsize=(8,6))

# Bar plot (counts)
ax1.bar(df["Defect"], df["Count"], color="lightgreen", edgecolor="black")
ax1.set_xlabel("Defect Type")
ax1.set_ylabel("Count", color="green")
ax1.tick_params(axis="y", labelcolor="green")

# Line plot (cumulative percentage)
ax2 = ax1.twinx()
ax2.plot(df["Defect"], df["CumulativePercent"], color="red", marker="o", linestyle="-")
ax2.set_ylabel("Cumulative Percentage (%)", color="red")
ax2.tick_params(axis="y", labelcolor="red")
ax2.set_ylim(0, 110)

plt.title("Pareto Chart - PCB Defects")
plt.savefig("pareto_chart.png")
plt.close()

print("✅ Charts saved as: bar_chart.png, histogram.png, pareto_chart.png\n")

# ----------------------------
# Task 4: Findings
# ----------------------------
print("=== Task 4: Findings ===\n")
top_defect = df.iloc[0]
print(f"The most common defect is '{top_defect['Defect']}' "
      f"with {top_defect['Count']} cases, contributing "
      f"{top_defect['Percent']:.1f}% of all defects.\n")
      
      
The most common defect is 'Soldering' with 68 cases, contributing 43.6% of all defects.
