import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
day_df = pd.read_csv("../data/day.csv", parse_dates=['dteday'])

# Mapping season and weathersit to readable labels
season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
weather_mapping = {1: "Clear", 2: "Cloudy", 3: "Rainy", 4: "Stormy"}

day_df['season_label'] = day_df['season'].map(season_mapping)
day_df['weather_label'] = day_df['weathersit'].map(weather_mapping)

# Sidebar Filters
st.sidebar.header("Filter Data")
selected_date = st.sidebar.date_input("Pilih Tanggal", day_df['dteday'].min())
selected_season = st.sidebar.selectbox(
    "Pilih Musim", list(season_mapping.values()))
selected_weather = st.sidebar.selectbox(
    "Pilih Kondisi Cuaca", list(weather_mapping.values()))

# Filter Data
filtered_df = day_df[
    (day_df['dteday'] == pd.to_datetime(selected_date)) &
    (day_df['season_label'] == selected_season) &
    (day_df['weather_label'] == selected_weather)
]

# Title
st.title("Bike Sharing Data Dashboard")

# Data Overview
st.subheader("Data Overview")
st.write(day_df.head())

# Tren Penggunaan Sepeda Sepanjang Tahun
st.subheader("Tren Penggunaan Sepeda Sepanjang Tahun")
monthly_trend = day_df.groupby(day_df['dteday'].dt.to_period("M")).agg({
    "cnt": "sum"}).reset_index()
plt.figure(figsize=(12, 5))
sns.lineplot(x=monthly_trend['dteday'].astype(
    str), y=monthly_trend['cnt'], color='blue')
plt.xticks(rotation=45)
plt.xlabel("Bulan")
plt.ylabel("Jumlah Peminjaman Sepeda")
plt.title("Tren Penggunaan Sepeda Sepanjang Tahun")
st.pyplot(plt)

# Distribusi Jumlah Peminjaman Sepeda (Boxplot)
st.subheader("Distribusi Jumlah Peminjaman Sepeda Harian")
plt.figure(figsize=(10, 6))
sns.boxplot(y=filtered_df['cnt'], color='skyblue')
plt.ylabel("Jumlah Peminjaman Sepeda")
plt.title("Distribusi Peminjaman Sepeda Harian")
st.pyplot(plt)

# Pengaruh Kondisi Cuaca terhadap Peminjaman Sepeda
st.subheader("Pengaruh Kondisi Cuaca terhadap Peminjaman Sepeda")
weather_impact = day_df.groupby("weather_label").agg(
    {"cnt": "mean"}).reset_index()
plt.figure(figsize=(10, 5))
sns.barplot(x=weather_impact['weather_label'],
            y=weather_impact['cnt'], palette='coolwarm')
plt.xlabel("Kondisi Cuaca")
plt.ylabel("Rata-rata Peminjaman Sepeda")
plt.title("Pengaruh Kondisi Cuaca terhadap Jumlah Peminjaman Sepeda")
st.pyplot(plt)

# Korelasi Antar Variabel
st.subheader("Heatmap Korelasi Antar Variabel")
numerical_day_df = day_df.select_dtypes(include=['number'])
plt.figure(figsize=(10, 6))
sns.heatmap(numerical_day_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
st.pyplot(plt)
