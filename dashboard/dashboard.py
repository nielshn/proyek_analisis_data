import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
day_df = pd.read_csv("../data/day.csv", parse_dates=['dteday'])

# Title
st.title("Bike Sharing Data Dashboard")

# Data Overview
st.subheader("Data Overview")
st.write(day_df.head())

# Data Cleaning Summary
st.subheader("Data Cleaning")
st.write("Data Harian Duplikat:", day_df.duplicated().sum())
st.write("Missing Values:", day_df.isna().sum().sum())

# Tren Penggunaan Sepeda Sepanjang Tahun
st.subheader("Tren Penggunaan Sepeda Sepanjang Tahun")
monthly_trend = day_df.groupby(day_df['dteday'].dt.to_period("M")).agg({
    "cnt": "sum"}).reset_index()
plt.figure(figsize=(12, 5))

sns.lineplot(
    x=monthly_trend['dteday'].astype(str),
    y=monthly_trend['cnt'],
    color='blue'
)
plt.xticks(rotation=45)
plt.xlabel("Bulan")
plt.ylabel("Jumlah Peminjaman Sepeda")
plt.title("Tren Penggunaan Sepeda Sepanjang Tahun")
st.pyplot(plt)

# Distribusi Jumlah Peminjaman Sepeda (Boxplot)
st.subheader("Distribusi Jumlah Peminjaman Sepeda Harian")
plt.figure(figsize=(10, 6))
sns.boxplot(y=day_df['cnt'], color='skyblue')
plt.ylabel("Jumlah Peminjaman Sepeda")
plt.title("Distribusi Peminjaman Sepeda Harian")
st.pyplot(plt)

# Pengaruh Kondisi Cuaca terhadap Peminjaman Sepeda
st.subheader("Pengaruh Kondisi Cuaca terhadap Peminjaman Sepeda")
weather_impact = day_df.groupby("weathersit").agg(
    {"cnt": "mean"}).reset_index()
plt.figure(figsize=(10, 5))
sns.barplot(x=weather_impact['weathersit'],
            y=weather_impact['cnt'], palette='coolwarm')
plt.xlabel("Kondisi Cuaca (1=Baik, 2=Normal, 3=Buruk, 4=Sangat Buruk)")
plt.ylabel("Rata-rata Peminjaman Sepeda")
plt.title("Pengaruh Kondisi Cuaca terhadap Jumlah Peminjaman Sepeda")
st.pyplot(plt)

# Korelasi Antar Variabel
st.subheader("Heatmap Korelasi Antar Variabel")
numerical_day_df = day_df.select_dtypes(include=['number'])
plt.figure(figsize=(10, 6))
sns.heatmap(numerical_day_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
st.pyplot(plt)
