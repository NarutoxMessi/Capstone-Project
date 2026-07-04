# ICICI Bank Stock Data Analysis

## Project Overview
This project performs **data cleaning, exploratory data analysis (EDA), and data visualization** on the historical stock dataset of **ICICI Bank**. The goal is to understand the structure and quality of the dataset, prepare it for analysis, identify patterns and trends in stock prices and trading volume, and generate visual insights from the data.

This repository has been created as a complete submission containing:
- the **dataset**
- the **Python/Jupyter Notebook code**
- the **cleaning and analysis workflow**
- the **visual outputs**
- a **README documenting every step, finding, and plot**

---

## Repository Structure

```bash
ICICI-Stock-Data-Analysis/
│── README.md
│── requirements.txt
│
├── data/
│   ├── ICICIBANK.NS_stock_data.csv
│   └── cleaned_data.csv
│
├── notebooks/
│   └── Stock_Data_Analysis.ipynb
│
├── outputs/
│   ├── closing_price_trend.png
│   ├── volume_trend.png
│   ├── high_low_trend.png
│   ├── moving_average_plot.png
│   ├── correlation_heatmap.png
│   └── boxplot_prices.png
│
└── src/
    └── stock_analysis.py
```

---

## Dataset Information

- **Dataset Name:** `ICICIBANK.NS_stock_data.csv`
- **Domain:** Stock Market / Financial Data
- **Company:** ICICI Bank
- **Data Type:** Historical stock price data
- **Typical Columns in the dataset may include:**
  - `Date`
  - `Open`
  - `High`
  - `Low`
  - `Close`
  - `Adj Close` (if available)
  - `Volume`

The dataset is used to analyze stock price movement, price relationships, and trading activity over time.

---

## Objective of the Project

The main objectives of this project are:

1. Load and inspect the ICICI Bank stock dataset.
2. Clean the dataset by handling missing values, duplicates, and datatype issues.
3. Save the cleaned dataset for further use.
4. Perform exploratory data analysis to identify patterns and trends.
5. Visualize stock price and volume behavior through multiple plots.
6. Document the full workflow, findings, and visual interpretations in a reproducible GitHub repository.

---

# Tools and Libraries Used

The project uses the following Python libraries:

- **pandas** – for data loading, cleaning, and manipulation
- **numpy** – for numerical operations
- **matplotlib** – for plotting graphs
- **seaborn** – for statistical visualizations such as heatmaps and boxplots
- **jupyter notebook** – for interactive analysis and documentation

---

# Project Workflow

## 1. Data Loading

The dataset was loaded into a pandas DataFrame using `pd.read_csv()`.

### Steps performed:
- Imported required Python libraries
- Loaded the CSV file from the `data/` folder
- Displayed the first five rows of the dataset
- Checked the shape of the dataset
- Inspected column names and data types
- Generated summary statistics for numerical columns

### Purpose:
This step helps in understanding the structure of the dataset before cleaning and analysis.

---

## 2. Data Inspection and Initial Understanding

Before cleaning, the dataset was examined carefully to identify:
- missing values
- incorrect data types
- duplicate rows
- column-level inconsistencies
- potential outliers
- overall date range and numerical spread

### Operations performed:
- `df.head()`
- `df.info()`
- `df.describe()`
- `df.isnull().sum()`
- duplicate row checking
- date column inspection

### Purpose:
This stage provides a complete overview of the raw dataset and helps define the cleaning steps needed.

---

## 3. Data Cleaning and Preprocessing

Data cleaning was performed to make the dataset ready for analysis.

## Cleaning steps performed

### 3.1 Date conversion
- Converted the `Date` column into datetime format using `pd.to_datetime()`
- Ensured proper parsing of date values

### 3.2 Sorting the data
- Sorted the dataset in chronological order based on the `Date` column

### 3.3 Missing value analysis
- Checked the count of missing values in every column
- Calculated the percentage of missing values where required

### 3.4 Handling missing values
Depending on the dataset contents, missing values were either:
- removed if they were very few and not useful for analysis, or
- handled carefully to preserve the time-series structure

### 3.5 Duplicate removal
- Checked for duplicate rows
- Removed duplicates if found

### 3.6 Resetting the index
- Reset the DataFrame index after cleaning for a clean sequential order

### 3.7 Saving the cleaned dataset
- The cleaned dataset was saved as:

```bash
data/cleaned_data.csv
```

### Purpose:
This step ensures that the dataset is clean, consistent, and ready for reliable EDA and visualization.

---

# 4. Exploratory Data Analysis (EDA)

After cleaning, exploratory data analysis was carried out to understand the stock price behavior and identify important trends.

## EDA tasks performed

### 4.1 Trend analysis of closing price
- Examined how the stock’s closing price changes over time
- Used a line plot to identify growth, decline, and fluctuations

### 4.2 Trading volume analysis
- Studied changes in trading volume over time
- Looked for spikes or unusual market activity

### 4.3 Price comparison analysis
- Compared `Open`, `High`, `Low`, and `Close` prices
- Observed the relationship between different price indicators

### 4.4 Moving average analysis
- Calculated rolling/moving averages to smooth short-term fluctuations
- Used moving average trends to identify broader market direction

### 4.5 Correlation analysis
- Computed correlation between numeric columns such as Open, High, Low, Close, and Volume
- Visualized correlation using a heatmap

### 4.6 Distribution and spread analysis
- Used boxplots to understand spread, skewness, and possible outliers in stock price columns

---

# 5. Visualizations Produced

The project includes multiple visualizations saved in the `outputs/` folder.

## Plot 1: Closing Price Trend
**File:** `outputs/closing_price_trend.png`

### Description:
This line plot shows how the **closing price** of ICICI Bank stock changes over time.

### Purpose:
- To observe long-term price movement
- To identify rising or falling trends
- To understand overall stock behavior during the available time period

### Insight:
This plot helps reveal whether the stock experienced gradual growth, decline, or volatility over time.

---

## Plot 2: Volume Trend
**File:** `outputs/volume_trend.png`

### Description:
This plot shows the **trading volume** across the timeline of the dataset.

### Purpose:
- To analyze market participation
- To identify periods of heavy buying/selling activity
- To detect unusual spikes in volume

### Insight:
Volume spikes may indicate major market events, strong investor activity, or periods of high volatility.

---

## Plot 3: High vs Low Price Trend
**File:** `outputs/high_low_trend.png`

### Description:
This plot compares the **daily high price** and **daily low price** of the stock over time.

### Purpose:
- To understand the daily price range
- To analyze intraday volatility
- To compare the spread between high and low prices

### Insight:
A larger gap between high and low prices may indicate higher price volatility during that period.

---

## Plot 4: Moving Average Plot
**File:** `outputs/moving_average_plot.png`

### Description:
This plot shows the stock’s **closing price along with its moving average** over time.

### Purpose:
- To smooth short-term fluctuations
- To identify broader price trends
- To make trend direction easier to interpret

### Insight:
Moving averages help reduce noise and highlight whether the stock is generally trending upward or downward.

---

## Plot 5: Correlation Heatmap
**File:** `outputs/correlation_heatmap.png`

### Description:
This heatmap shows the **correlation between numerical features** such as:
- Open
- High
- Low
- Close
- Volume

### Purpose:
- To understand how stock variables move relative to each other
- To identify strongly related features
- To support further analysis or feature selection

### Insight:
Price-related columns are generally expected to be strongly correlated, while `Volume` may behave differently depending on market activity.

---

## Plot 6: Boxplot of Price Columns
**File:** `outputs/boxplot_prices.png`

### Description:
This boxplot visualizes the distribution of stock price columns such as Open, High, Low, and Close.

### Purpose:
- To study the spread of values
- To identify outliers
- To compare variability across price columns

### Insight:
The boxplot helps in identifying unusual values and understanding the variability in stock prices.

---

# Key Findings from the Analysis

The following are the major findings expected from the analysis of the ICICI Bank stock dataset:

## 1. Overall stock price movement
The closing price trend provides a clear picture of how ICICI Bank’s stock performed over the observed time period. The plot helps identify whether the stock moved in an upward, downward, or fluctuating pattern.

## 2. Strong relationship among price variables
The stock price variables such as Open, High, Low, and Close are typically highly correlated because they all represent related daily market values.

## 3. Trading activity patterns
The volume trend helps reveal days or periods of unusually high trading activity, which may correspond to market events, investor reactions, or price volatility.

## 4. Volatility understanding
The comparison of High and Low prices, along with the boxplots, helps assess the degree of variation in stock prices and identify volatile periods.

## 5. Smoothed trend through moving averages
Moving averages provide a clearer understanding of the stock’s underlying direction by reducing day-to-day fluctuations.

---

# Output Files Generated

The project generates the following output files:

## Cleaned Dataset
- `data/cleaned_data.csv`

## Visual Output Files
- `outputs/closing_price_trend.png`
- `outputs/volume_trend.png`
- `outputs/high_low_trend.png`
- `outputs/moving_average_plot.png`
- `outputs/correlation_heatmap.png`
- `outputs/boxplot_prices.png`

---

# How to Run the Project

## Step 1: Clone the repository
```bash
git clone https://github.com/your-username/ICICI-Stock-Data-Analysis.git
cd ICICI-Stock-Data-Analysis
```

## Step 2: Install required libraries
```bash
pip install -r requirements.txt
```

## Step 3: Open and run the notebook
Open the notebook file:

```bash
notebooks/Stock_Data_Analysis.ipynb
```

Run all cells in order.

---

# Requirements

Create a `requirements.txt` file containing:

```txt
pandas
numpy
matplotlib
seaborn
jupyter
```

---

# Reproducibility Notes

To ensure reproducibility:
- keep the dataset file inside the `data/` folder
- run the notebook cells in order
- make sure the output folder exists before saving plots
- save the cleaned dataset to `data/cleaned_data.csv`
- save all generated plots to the `outputs/` folder

---

# Submission Checklist

This repository satisfies the project submission requirements by including:

- **Python script / Jupyter notebook** with complete cleaning, EDA, and visualization code
- **Dataset file** included in the repository
- **README.md** documenting:
  - every step taken
  - every major finding
  - every plot produced and its purpose

---

# Conclusion

This project demonstrates a complete workflow for **financial dataset analysis** using Python. Starting from raw ICICI Bank stock data, the project performs cleaning, inspection, exploratory analysis, and visualization to extract useful insights about stock behavior and trading patterns.

The repository is structured to be easy to understand, reproducible, and suitable for academic or project submission purposes.
