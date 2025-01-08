import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


Ourdata = ('global_air_pollution_data.csv')
## Pi chart for aqi 
def plot_aqi_pie_chart(file_path):
    ## Load dataset
    data = pd.read_csv(file_path)

    ## Count the occurrences of each AQI category
    aqi_counts = data['aqi_category'].value_counts()
    ## Calculate the percentage for each category
    percentages = 100 * aqi_counts / aqi_counts.sum()

    ## pie chart
    fig, ax = plt.subplots(figsize=(8, 8))  
    colors = plt.get_cmap('tab20')(range(len(aqi_counts))) 
    wedges, texts, autotexts = ax.pie(aqi_counts, 
                                      autopct='%1.1f%%',  
                                      startangle=90, 
                                      colors=colors, 
                                      labeldistance=1.2, 
                                      wedgeprops={'edgecolor': 'black'})

    ## Title and legend with percentage
    plt.title('Distribution of AQI Categories')
    plt.ylabel('')  

    ## Creating the legend with both category and percentage since it looks so squished without it. 
    legend_labels = [f'{category}: {percentage:.1f}%' for category, percentage in zip(aqi_counts.index, percentages)]
    ax.legend(wedges, legend_labels, title="AQI Categories", loc="center left", bbox_to_anchor=(1, 0.5))

    plt.tight_layout()
    plt.show()


def analyze_average_aqi(file_path):
    ## reading the data
    data = pd.read_csv(file_path)
    ## finding the mean of all the countries 
    country_means = data.groupby('country_name')['aqi_value'].mean().sort_values(ascending=False)
    ## gets the top 10 countries and plots
    top_10 = country_means.head(10)
    plt.figure(figsize=(10, 6))
    top_10.plot(kind='bar', color='red', edgecolor='black')
    ## titles and stuff
    plt.title('Top 10 Countries by Average AQI')
    plt.ylabel('Average AQI')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def create_boxplot_aqi_by_category(file_path):
    ## Reading the data
    df = pd.read_csv(file_path)
    plt.figure(figsize=(10, 6))

    ## box plot
    sns.boxplot(x='aqi_category', y='aqi_value', data=df)


    plt.title('Distribution of AQI by Category')
    plt.xlabel('AQI Category')
    plt.ylabel('AQI Value')
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


plot_aqi_pie_chart(Ourdata)
analyze_average_aqi(Ourdata)
create_boxplot_aqi_by_category(Ourdata)