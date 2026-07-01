import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv("ecommerce_return_analysis_4000.csv")

# Check Missing Values
print(df.isnull().sum())

# Fill Missing Values
df['age'] = df['age'].fillna(df['age'].median())
df['marketing_channel'] = df['marketing_channel'].fillna('Unknown')
df['returned'] = df['returned'].fillna('No')
df['return_reason'] = df['return_reason'].fillna('Not Specified')

# Check Duplicates
print("Duplicates:", df.duplicated().sum())

# Remove Duplicates
df = df.drop_duplicates()

# Check Categories
print(df['category'].unique())

# Boxplot for Outliers
plt.boxplot(df['product_price'])
plt.title("Product Price Distribution")
plt.show()

# IQR Calculation
Q1 = df['product_price'].quantile(0.25)
Q3 = df['product_price'].quantile(0.75)
IQR = Q3 - Q1

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)

# Create Return Flag
df['return_flag'] = df['returned'].map({
    'Yes': 1,
    'No': 0
})

# Overall Return Rate
return_rate = df['return_flag'].mean() * 100
print("Overall Return Rate:", round(return_rate, 2), "%")

# Return Rate by Category
category_return = (
    df.groupby('category')['return_flag']
      .mean() * 100
)

print(category_return)

# Return Rate by State
state_return = (
    df.groupby('state')['return_flag']
      .mean() * 100
      .sort_values(ascending=False)
)

print(state_return.head())

# Return Rate by Marketing Channel
channel_return = (
    df.groupby('marketing_channel')['return_flag']
      .mean() * 100
      .sort_values(ascending=False)
)

print(channel_return)

# Category Chart
category_return.plot(
    kind='bar',
    figsize=(8,5)
)

plt.title("Return Rate by Category")
plt.ylabel("Return Rate (%)")
plt.show()

# Marketing Channel Chart
channel_return.plot(
    kind='bar',
    figsize=(8,5)
)

plt.title("Return Rate by Marketing Channel")
plt.ylabel("Return Rate (%)")
plt.show()

# Save Cleaned Data
df.to_csv(
    'cleaned_data.csv',
    index=False
)

print("Cleaned dataset saved successfully.")