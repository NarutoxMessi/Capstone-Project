# part1_data_preparation.py

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1. Create folders if not present
# -----------------------------
os.makedirs("data", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# -----------------------------
# 2. Load dataset
# -----------------------------
file_path = "data/ICICIBANK.NS_stock_data.csv"   # place your dataset here
df = pd.read_csv(file_path)

print("First 5 rows of dataset:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nSummary Statistics:")
print(df.describe())

# -----------------------------
# 3. Null value analysis
# -----------------------------
print("\nMissing Values Count:")
missing_count = df.isnull().sum()
print(missing_count)

print("\nMissing Values Percentage:")
missing_percentage = (df.isnull().sum() / len(df)) * 100
print(missing_percentage)

# -----------------------------
# 4. Data Cleaning
# -----------------------------

# Convert Date column to datetime if present
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.sort_values("Date")

# Remove duplicate rows
df = df.drop_duplicates()

# Drop rows with missing Date if Date exists
if "Date" in df.columns:
    df = df.dropna(subset=["Date"])

# Fill missing numeric values with forward fill then backward fill
numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].ffill().bfill()

# Reset index
df = df.reset_index(drop=True)

print("\nCleaned Dataset Info:")
print(df.info())

print("\nCleaned Dataset Preview:")
print(df.head())

# -----------------------------
# 5. Save cleaned dataset
# -----------------------------
cleaned_file_path = "data/cleaned_data.csv"
df.to_csv(cleaned_file_path, index=False)
print(f"\nCleaned dataset saved to: {cleaned_file_path}")

# -----------------------------
# 6. Basic EDA + Visualizations
# -----------------------------
sns.set(style="whitegrid")

# Closing Price Trend
if "Date" in df.columns and "Close" in df.columns:
    plt.figure(figsize=(12, 6))
    plt.plot(df["Date"], df["Close"])
    plt.title("Closing Price Trend")
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("outputs/closing_price_trend.png")
    plt.close()

# Volume Trend
if "Date" in df.columns and "Volume" in df.columns:
    plt.figure(figsize=(12, 6))
    plt.plot(df["Date"], df["Volume"])
    plt.title("Volume Trend")
    plt.xlabel("Date")
    plt.ylabel("Volume")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("outputs/volume_trend.png")
    plt.close()

# High vs Low Trend
if "Date" in df.columns and "High" in df.columns and "Low" in df.columns:
    plt.figure(figsize=(12, 6))
    plt.plot(df["Date"], df["High"], label="High")
    plt.plot(df["Date"], df["Low"], label="Low")
    plt.title("High vs Low Price Trend")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("outputs/high_low_trend.png")
    plt.close()

# Moving Average Plot
if "Close" in df.columns and "Date" in df.columns:
    df["Moving_Avg_20"] = df["Close"].rolling(window=20).mean()
    plt.figure(figsize=(12, 6))
    plt.plot(df["Date"], df["Close"], label="Close")
    plt.plot(df["Date"], df["Moving_Avg_20"], label="20-Day Moving Avg")
    plt.title("Closing Price with Moving Average")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("outputs/moving_average_plot.png")
    plt.close()

# Correlation Heatmap
numeric_df = df.select_dtypes(include=[np.number])
if not numeric_df.empty:
    plt.figure(figsize=(10, 6))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("outputs/correlation_heatmap.png")
    plt.close()

# Boxplot for price columns
price_cols = [col for col in ["Open", "High", "Low", "Close"] if col in df.columns]
if price_cols:
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df[price_cols])
    plt.title("Boxplot of Price Columns")
    plt.tight_layout()
    plt.savefig("outputs/boxplot_prices.png")
    plt.close()

print("\nAll outputs saved successfully in outputs/ folder.")
