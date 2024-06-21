# Overview

This dataset analysis software code was written to clean up the final-house dataset then analyze it to answers three questions about the obtained data (provided in the Data Analysis Results section below). It also creates charts and graphs from the provided data for further analyzation and dissection of information.

[The final-house dataset used with this software can be found here.](https://www.kaggle.com/datasets/rukenmissonnier/final-house/data)

[Software Demo Video](http://youtube.link.goes.here)

# Data Analysis Results

1. What factors influence house prices the most in this dataset?
- Number of Bedrooms: Houses with 17 bedrooms tend to have the highest average price.
- Floor Level: Houses on floor 1 have the highest average price.
- Age of the House: There is a correlation coefficient of -0.23 between age and price, indicating a slight negative influence.
- Center Distance: There is a correlation coefficient of -0.42 between distance from center and price, indicating a moderate negative influence.
- Metro Distance: There is a correlation coefficient of -0.15 between distance from metro and price, indicating a slight negative influence.

2. What are the trends and demands in the housing market based on the given data?
- Bedroom Demand: Houses with 2 bedrooms are most frequently listed.
- Floor Demand: Houses on floor 1 are most frequently listed.

3. How does the age of the house correlate with the price or floor level?
- Correlation with Price: There is a correlation coefficient of -0.23 between age of the house and price.
- Correlation with Floor Level: There is a correlation coefficient of 0.02 between age of the house and floor level.

# Development Environment

Visual Studio Code was used in the creation of this software.

The programming language used is Python. Extensions used for the purposes of converting the dataset into charts included Pandas, Matplotlib.pyplot, and Seaborn.

# Useful Websites

* [Bioinformatics Pandas Python Tutorial for Beginners](https://www.youtube.com/watch?v=eAjZAnsg9ek)
* [W3 Schools Pandas Tutorial](https://www.w3schools.com/python/pandas/default.asp)
* [W3 Schools Matplotlib Pyplot Tutorial](https://www.w3schools.com/python/matplotlib_pyplot.asp)
* [Derek Banas Seaborn Tutorial: Seaborn Full Course](https://www.youtube.com/watch?v=6GUZXDef2U0)

# Future Work

* Create a method to save the generated graphs in a usable format.
* Rewrite the code so it can handle other datasets using the .csv format.
* Remove the hard coding of the answers and replace them with a more dynamic system that changes with the answers provided (like if the correlation coefficients was positive for the first question)
