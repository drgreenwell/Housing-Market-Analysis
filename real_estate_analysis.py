import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Answers to questions
# Trend by number of bedrooms
bedroom_influence = df.groupby('bedroom_count')['price'].mean()
bedroom_influence = bedroom_influence.sort_values(ascending=False).index[0]

# Trend by floor
floor_influence = df.groupby('floor')['price'].mean()
floor_influence = floor_influence.sort_values(ascending=False).index[0]

# Trend by age of the house
age_influence = df[['age', 'price']].corr().loc['age', 'price']

# Analyze housing demand
# Distribution of listings by number of bedrooms
bedroom_demand = df['bedroom_count'].value_counts().idxmax()

# Distribution of listings by floor
floor_demand = df['floor'].value_counts().idxmax()

# Regional variations
# Price vs. center distance
center_distance_influence = df[['center_distance', 'price']].corr().loc['center_distance', 'price']

# Price vs. metro distance
metro_distance_influence = df[['metro_distance', 'price']].corr().loc['metro_distance', 'price']

# Correlation between age of the house and other factors
age_corr_with_price = df[['age', 'price']].corr().loc['age', 'price']
age_corr_with_floor = df[['age', 'floor']].corr().loc['age', 'floor']

# Print answers to questions
print("\nAnswers based on analysis of 'house.csv':\n")
print("1. What factors influence house prices the most in this dataset?")
print(f"- Number of Bedrooms: Houses with {bedroom_influence} bedrooms tend to have the highest average price.")
print(f"- Floor Level: Houses on floor {floor_influence} have the highest average price.")
print(f"- Age of the House: There is a correlation coefficient of {age_influence:.2f} between age and price, indicating a moderate negative influence.")
print(f"- Center Distance: There is a correlation coefficient of {center_distance_influence:.2f} between distance from center and price, indicating a slight negative influence.")
print(f"- Metro Distance: There is a correlation coefficient of {metro_distance_influence:.2f} between distance from metro and price, indicating a slight negative influence.")

print("\n2. What are the trends and demands in the housing market based on the given data?")
print(f"- Bedroom Demand: Houses with {bedroom_demand} bedrooms are most frequently listed.")
print(f"- Floor Demand: Houses on floor {floor_demand} are most frequently listed.")

print("\n3. How does the age of the house correlate with the price or floor level?")
print(f"- Correlation with Price: There is a correlation coefficient of {age_corr_with_price:.2f} between age of the house and price.")
print(f"- Correlation with Floor Level: There is a correlation coefficient of {age_corr_with_floor:.2f} between age of the house and floor level.")