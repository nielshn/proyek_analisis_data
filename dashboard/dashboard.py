import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
day_df = pd.read_csv("data/day.csv", parse_dates=['dteday'])
hour_df = pd.read_csv("data/hour.csv", parse_dates=['dteday'])

# Merge dataset
all_df = pd.merge(hour_df, day_df[['dteday', 'cnt']],
                  on='dteday', suffixes=('_hour', '_day'))
all_df.to_csv("all_data.csv", index=False)

st.title("Bike Sharing Dashboard")
st.sidebar.header("Filter Data")

# Data Filter
date_range = st.sidebar.date_input(
    "Select Data Range", [all_df['dteday'].min(), all_df['dteday'].max()])
filtered_df = all_df[(all_df['dteday'] >= pd.to_datetime(date_range[0])) & (
    all_df['dteday'] <= pd.to_datetime(date_range[1]))]

# Line Chart: Tren Pengguaan Sepeda
st.subheader("Tren Pengguaan Sepeda Sepanjang Tahun")
fig, ax = plt.subplots(figsize=(12, 5))
sns.lineplot(
    x=filtered_df['dteday'],
    y=filtered_df['cnt_day'],
    color='blue',
    ax=ax
)
plt.xlabel("Tanggal")
plt.ylabel("Jumlah Peminjaman Sepeda")
st.pyplot(fig)

# Boxplot: Pengaruh Cuaca terhadap Peminjaman Sepeda
st.subheader("Pengaruh Kondisi Cuaca terhadap Peminjaman Sepeda")
fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(
    x=filtered_df['weathersit'],
    y=filtered_df['cnt_day'],
    palette='coolwarm',
    ax=ax
)
plt.xlabel("Kondisi Cuaca (1=Baik, 2=Normal, 3=Buruk, 4=Sangat Buruk)")
plt.ylabel("Jumlah Peminjaman Sepeda")
st.pyplot(fig)

# Show Dataset
st.subheader("Dataset")
st.dataframe(filtered_df.head())
