import pandas as pd
import matplotlib.pyplot as plt

# Loading dataset
data = pd.read_csv("global_air_pollution_data.csv")

# Count the occurrences of each AQI category
aqi_counts = data['aqi_category'].value_counts()

# Calculate the percentage for each category
percentages = 100 * aqi_counts / aqi_counts.sum()

# Plot the pie chart
fig, ax = plt.subplots(figsize=(8, 8))  
colors = plt.get_cmap('tab20')(range(len(aqi_counts))) 
wedges, texts, autotexts = ax.pie(aqi_counts, 
                                  autopct='%1.1f%%',  
                                  startangle=90, 
                                  colors=colors, 
                                  labeldistance=1.2, 
                                  wedgeprops={'edgecolor': 'black'})

# Title and legend with percentage
plt.title('Distribution of AQI Categories')
plt.ylabel('')  

# Create the legend with both category and percentage
legend_labels = [f'{category}: {percentage:.1f}%' for category, percentage in zip(aqi_counts.index, percentages)]
ax.legend(wedges, legend_labels, title="AQI Categories", loc="center left", bbox_to_anchor=(1, 0.5))

# Show plot
plt.tight_layout()
plt.show()
