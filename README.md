# DAT5902 Final Project: Global Air Pollution Data Analysis

This repository contains a data analysis project focused on global air pollution data. The analysis includes generating visualizations and performing statistical computations to understand the distribution and trends in air quality across different regions.

## Table of Contents
1. [Project Description](#project-description)
2. [Dataset Overview](#dataset-overview)
3. [Features](#features)
4. [Installation](#installation)
8. [Repository Structure](#repository-structure)

---

## Project Description

The aim of this project is to analyze air quality data from cities worldwide, focusing on:
- Distribution of AQI (Air Quality Index) categories.
- Top countries by average AQI.
- Statistical variations in AQI values based on categories.

The results are visualized using pie charts, bar graphs, and boxplots, offering insights into global air pollution trends.

---

## Dataset Overview

The dataset used for this analysis is `global_air_pollution_data.csv`, containing the following columns:
- Link to the dataset : https://www.kaggle.com/datasets/sazidthe1/global-air-pollution-data/data

- **country_name**: Name of the country.
- **city_name**: Name of the city.
- **aqi_value**: Air Quality Index value.
- **aqi_category**: Category of the AQI value (e.g., Good, Moderate, Unhealthy).
- **co_aqi_value**: AQI value for Carbon Monoxide.
- **co_aqi_category**: Category for Carbon Monoxide AQI.
- **ozone_aqi_value**: AQI value for Ozone.
- **ozone_aqi_category**: Category for Ozone AQI.
- **no2_aqi_value**: AQI value for Nitrogen Dioxide.
- **no2_aqi_category**: Category for Nitrogen Dioxide AQI.
- **pm2.5_aqi_value**: AQI value for Particulate Matter (PM2.5).
- **pm2.5_aqi_category**: Category for PM2.5 AQI.

---

## Features

- **Pie Chart**: Visualizes the percentage distribution of AQI categories globally.
- **Bar Graph**: Highlights the top 10 countries with the highest average AQI.
- **Boxplot**: Shows the distribution of AQI values across different AQI categories.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installing Dependencies
- To ensure the project works seamlessly, you need to install the required Python libraries. Run the following command in your terminal:
    - pip install pandas matplotlib seaborn pytest os


### Cloning the repository
- Clone the repository:
   ```bash
   git clone https://github.com/Asim-Dhakal/DAT5902-FinalProject.git
   cd DAT5902-FinalProject


## repository-structure 

- DAT5902-FinalProject/
- ├── analysis.py             # Analysis functions and visualizations
- ├── test_suite.py           # Test suite for analysis functions
- ├── global_air_pollution_data.csv # Dataset
- ├── README.md               # Project documentation
- ├── .circleci/              # CircleCI configuration
- │   └── config.yml
