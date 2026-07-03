# Capstone-Project
# ICICI Bank Stock Data – AI & ML Capstone Project (Part 1)

## 1. Project Overview
This project performs Data Preparation and Exploration on 5-year ICICI Bank stock market data as part of the IIT Patna AI & ML Capstone.

## 2. Dataset
- File: ICICIBANK.NS_stock_data.csv
- Columns: Date, open, high, low, close, adjclose, volume, ticker

## 3. Objectives of Part 1
- Load and inspect the dataset
- Analyze missing values
- Detect and remove duplicates
- Correct data types
- Compute descriptive statistics and skewness
- Detect outliers using IQR
- Generate required visualizations
- Compare Pearson and Spearman correlation
- Perform grouped aggregation
- Save cleaned dataset for later parts

## 4. Tools and Libraries
- Python
- pandas
- numpy
- matplotlib
- seaborn

## 5. Data Cleaning Steps
### 5.1 Missing Value Handling
Explain null count and percentage.
Mention that numeric columns below 20% null were filled using median.

### 5.2 Why Median Instead of Mean
Median is less affected by extreme stock price spikes or unusual trading volume.

### 5.3 Duplicate Removal
State how many duplicate rows were removed.

### 5.4 Data Type Correction
- Date converted to datetime
- ticker converted to category
- day_name converted to category

## 6. Feature Engineering
- year
- month
- day_name
- price_range
- daily_return
- volume_category

## 7. Descriptive Statistics and Skewness
Mention the most skewed numeric column and explain positive/negative skew.

## 8. Outlier Analysis
Describe outliers found in volume and daily_return.
State whether you plan to retain, cap, or handle them in Part 2.

## 9. Visualizations
### 9.1 Line Plot
Closing price over time.

### 9.2 Bar Chart
Average closing price by day of week.

### 9.3 Histogram
Most skewed column distribution.

### 9.4 Scatter Plot
Open vs close price relationship.

### 9.5 Box Plot
Close price distribution across day_name.

## 10. Correlation Analysis
### Pearson correlation heatmap
Mention the highest correlation pair.

### Spearman correlation
Discuss top 3 pairs with largest Spearman–Pearson differences.

## 11. Grouped Aggregation
Grouped mean, std, count of close by day_name.

## 12. Output
- cleaned_data.csv
- plots saved in outputs folder

## 13. Repository Structure
Show the folder structure.

## 14. Conclusion
Summarize the Part 1 work and state that cleaned_data.csv will be used in Parts 2 and 3.
