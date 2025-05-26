# Bike Collection Dashboard ✨

## Deskripsi

Dashboard ini dibuat menggunakan Streamlit untuk menganalisis data peminjaman sepeda berdasarkan tren tahunan dan pengaruh kondisi cuaca.

## Akses Dashboard Online

Kunjungi dashboard secara publik melalui tautan berikut:  
[https://nielshn.streamlit.app/](https://nielshn.streamlit.app/)

## Persyaratan

Sebelum menjalankan aplikasi, pastikan Anda memiliki Python 3.9 dan telah menginstal semua dependensi yang dibutuhkan.

## Setup Environment

### Menggunakan Anaconda:

```sh
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

### Menggunakan Shell/Terminal:

```sh
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Menjalankan Aplikasi Streamlit

Setelah lingkungan berhasil diatur, jalankan perintah berikut untuk menjalankan dashboard:

```sh
streamlit run dashboard.py
```

## Fitur Dashboard

- **Tren Penggunaan Sepeda**: Menampilkan grafik perubahan jumlah peminjaman sepeda sepanjang tahun.
- **Pengaruh Cuaca**: Visualisasi dampak kondisi cuaca terhadap jumlah peminjaman.
- **Filter Interaktif**: Memungkinkan pengguna untuk menyesuaikan periode waktu analisis.

## Kontributor

- Nama: Daniel Siahaan
- Email: niel.shn08@gmail.com
- Project: Bike Sharing Data Analysis
