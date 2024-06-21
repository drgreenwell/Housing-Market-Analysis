import pandas as pd
import matplotlib.pyplot as plt # Handles the overall plot layout and rendering
import seaborn as sns # Visualizes data using pair plots

# Load the data
file_path = 'house.csv'
df = pd.read_csv(file_path)

# Display basic information about the dataset
print(df.info())
print(df.describe())

# Clean and preprocess the data (if necessary)
# For example, handle missing values or outliers
df = df.dropna()  # Dropping missing values, if any
# Further cleaning steps can be added based on the data inspection

# Analyze price trends
# Trend by number of bedrooms
plt.figure(figsize=(10, 6))
sns.boxplot(x='bedroom_count', y='price', data=df)
plt.title('Price Trends by Number of Bedrooms')
plt.xlabel('Number of Bedrooms')
plt.ylabel('Price')
plt.show()

# Trend by floor
plt.figure(figsize=(10, 6))
sns.boxplot(x='floor', y='price', data=df)
plt.title('Price Trends by Floor')
plt.xlabel('Floor')
plt.ylabel('Price')
plt.show()

# Trend by age of the house
plt.figure(figsize=(10, 6))
sns.scatterplot(x='age', y='price', data=df)
plt.title('Price Trends by Age of House')
plt.xlabel('Age of House')
plt.ylabel('Price')
plt.show()

# Analyze housing demand
# Distribution of listings by number of bedrooms
plt.figure(figsize=(10, 6))
sns.countplot(x='bedroom_count', data=df)
plt.title('Distribution of Listings by Number of Bedrooms')
plt.xlabel('Number of Bedrooms')
plt.ylabel('Number of Listings')
plt.show()

# Distribution of listings by floor
plt.figure(figsize=(10, 6))
sns.countplot(x='floor', data=df)
plt.title('Distribution of Listings by Floor')
plt.xlabel('Floor')
plt.ylabel('Number of Listings')
plt.show()

# Analyze regional variations
# Price vs. center distance
plt.figure(figsize=(10, 6))
sns.scatterplot(x='center_distance', y='price', data=df)
plt.title('Price vs. Center Distance')
plt.xlabel('Distance from Center')
plt.ylabel('Price')
plt.show()

# Price vs. metro distance
plt.figure(figsize=(10, 6))
sns.scatterplot(x='metro_distance', y='price', data=df)
plt.title('Price vs. Metro Distance')
plt.xlabel('Distance from Metro')
plt.ylabel('Price')
plt.show()

# Additional analysis: Heatmap of correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

# Summary statistics for regional variations
print("Summary statistics for Center Distance:")
print(df['center_distance'].describe())
print("\nSummary statistics for Metro Distance:")
print(df['metro_distance'].describe())

# Analyzing relationship between different variables
sns.pairplot(df)
plt.show()