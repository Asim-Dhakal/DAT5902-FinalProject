import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("global_air_pollution_data.csv")

# Count the occurrences of each AQI category
aqi_counts = data['aqi_category'].value_counts()

# Plot the pie chart
plt.figure(figsize=(8, 8))  # This line should work after reinstalling matplotlib
aqi_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colormap='tab20')
plt.title('Distribution of AQI Categories')
plt.ylabel('')  # Remove default ylabel
plt.show()
