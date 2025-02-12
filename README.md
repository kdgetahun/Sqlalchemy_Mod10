# Climate Analysis and API Development

## Overview
This project involves analyzing climate data for Honolulu, Hawaii, to help with trip planning. Using Python, SQLAlchemy, Pandas, and Matplotlib, we explore historical weather data and create a Flask API to provide climate insights.

## Technologies Used
- **Python**
- **SQLAlchemy** (ORM & Queries)
- **Pandas**
- **Matplotlib**
- **Flask** (API Development)
- **SQLite**

## Project Structure
The project consists of two main parts:

### Part 1: Climate Data Analysis
Using SQLAlchemy and Pandas, I perform the following analyses on historical climate data:

#### 1. Precipitation Analysis
- Extracts the most recent date from the dataset.
- Queries the last 12 months of precipitation data.
- Stores the results in a Pandas DataFrame, sorts by date, and visualizes precipitation trends using a plot.
- Displays summary statistics of the precipitation data.

#### 2. Station Analysis
- Determines the total number of weather observation stations.
- Identifies the most active station based on observation counts.
- Calculates minimum, maximum, and average temperatures for the most active station.
- Extracts and visualizes the last 12 months of temperature observations using a histogram.

### Part 2: Flask API Development
Develop a Flask application that provides climate data through various endpoints:



- - -

