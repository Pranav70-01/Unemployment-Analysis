# 1: Here i am importing the required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#  2: Load dataset
try:
    df = pd.read_csv("unemployment_data.csv")
except FileNotFoundError:
    print("Error: Dataset file not found. Make sure 'unemployment_data.csv' is in the same folder.")
    exit()

#  3: Cleaning column names 
df.columns = df.columns.str.strip()

#  4: Cleaning data values 
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype(str).str.strip()

#  5: Check and display missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

#  6: Droping rows with any missing values
df_cleaned = df.dropna()

print("\nData cleaned. Rows before:", len(df), "→ after:", len(df_cleaned))

#  7: Basic Exploration
print("\nFirst 5 rows of cleaned dataset:")
print(df_cleaned.head())

print("\nDataset info after cleaning:")
print(df_cleaned.info())

print("\nSummary statistics:")
print(df_cleaned.describe())

#  8: Descriptive Analysis
avg_unemp = df_cleaned['Estimated Unemployment Rate (%)'].mean()
max_unemp = df_cleaned['Estimated Unemployment Rate (%)'].max()
min_unemp = df_cleaned['Estimated Unemployment Rate (%)'].min()

print(f"\nAverage unemployment rate in dataset: {avg_unemp:.2f}%")
print(f"Maximum unemployment rate: {max_unemp}%")
print(f"Minimum unemployment rate: {min_unemp}%")

#  9: Region-wise Unemployment Rate
print("\nAverage unemployment rate by Region:")
print(df_cleaned.groupby("Region")['Estimated Unemployment Rate (%)'].mean())

#  10: Save cleaned data to CSV
df_cleaned.to_csv("cleaned_unemployment_data.csv", index=False)
print("\nCleaned data saved to 'cleaned_unemployment_data.csv'.")

#  11: Visualization - Unemployment Rate by Region
print("\nGenerating plot: Average Unemployment Rate by Region...")
plt.figure(figsize=(14, 7))
sns.set(style="whitegrid")
region_unemp = df_cleaned.groupby("Region")['Estimated Unemployment Rate (%)'].mean().sort_values(ascending=False)

# Bar plot
sns.barplot(x=region_unemp.index, y=region_unemp.values, palette="viridis")
plt.xticks(rotation=90)
plt.xlabel("Region")
plt.ylabel("Average Unemployment Rate (%)")
plt.title("Average Unemployment Rate by Region")
plt.tight_layout()
plt.show()

 