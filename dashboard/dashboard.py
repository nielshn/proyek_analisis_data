import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load dataset
day_df = pd.read_csv("data/day.csv", parse_dates=['dteday'])

# Mapping season and weathersit to readable labels
season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
weather_mapping = {1: "Clear", 2: "Cloudy", 3: "Rainy", 4: "Stormy"}

day_df['season_label'] = day_df['season'].map(season_mapping)
day_df['weather_label'] = day_df['weathersit'].map(weather_mapping)

# rentang tanggal dari dataset
min_date = day_df["dteday"].min()
max_date = day_df["dteday"].max()

# Sidebar Filters
st.sidebar.header("Filter Data")

date_range = st.sidebar.date_input(
    "Pilih Rentang Tanggal",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Pastikan input date_range memiliki dua nilai
if isinstance(date_range, tuple) and len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date, end_date = min_date, max_date

selected_season = st.sidebar.multiselect(
    "Pilih Musim", list(season_mapping.values()),
    default=list(season_mapping.values())
)
selected_weather = st.sidebar.multiselect(
    "Pilih Kondisi Cuaca", list(weather_mapping.values()),
    default=list(weather_mapping.values())
)

# Filter Data
filtered_df = day_df[
    (day_df['dteday'] >= pd.to_datetime(start_date)) &
    (day_df['dteday'] <= pd.to_datetime(end_date)) &
    (day_df['season_label'].isin(selected_season)) &
    (day_df['weather_label'].isin(selected_weather))
]


# handling for empty filter
if filtered_df.empty:
    st.warning("Tidak ada data yang sesuai dengan fitler yang dipilih.")
    st.stop()

# Title
st.title("Bike Sharing Data Dashboard")

# Data Overview
st.subheader("Data Overview")
st.write(filtered_df.head())

# Tren Penggunaan Sepeda Sepanjang Tahun
st.subheader("Tren Penggunaan Sepeda Sepanjang Tahun")
monthly_trend = filtered_df.groupby(
    filtered_df['dteday'].dt.to_period("M")).agg({"cnt": "sum"}).reset_index()

plt.figure(figsize=(12, 5))
sns.barplot(
    x=monthly_trend['dteday'].astype(str),
    y=monthly_trend['cnt'],
    color='skyblue'
)
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
weather_impact = filtered_df.groupby(
    "weather_label").agg({"cnt": "mean"}).reset_index()
plt.figure(figsize=(10, 5))
sns.barplot(x=weather_impact['weather_label'],
            y=weather_impact['cnt'], palette='coolwarm')
plt.xlabel("Kondisi Cuaca")
plt.ylabel("Rata-rata Peminjaman Sepeda")
plt.title("Pengaruh Kondisi Cuaca terhadap Jumlah Peminjaman Sepeda")
st.pyplot(plt)

# Korelasi Antar Variabel
st.subheader("Heatmap Korelasi Antar Variabel")
numerical_day_df = filtered_df.select_dtypes(include=['number'])
plt.figure(figsize=(10, 6))
sns.heatmap(numerical_day_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
st.pyplot(plt)
