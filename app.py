import streamlit as st
import pandas as pd

import analisis as ana 

st.set_page_config(page_title="Dashboard Traveloka Analis", page_icon="✈️", layout="wide")
st.title("📊 Dashboard Analisis Data Traveloka")
st.markdown("Dashboard interaktif kelompok hasil integrasi modul `analisis.py` dan Streamlit UI.")
st.write("---")

try:
    df_kuesioner, df_playstore = ana.load_data()
except Exception as e:
    st.error("Gagal membaca data! Pastikan file 'data_traveloka_200_playstore.xlsx' berada di folder yang sama.")
    st.stop()

tab_gform, tab_playstore = st.tabs(["📋 Data Kuesioner (GForm)", "🤖 Data Scraping (Play Store)"])

with tab_gform:
    st.header("Analisis Persepsi & Profil Responden")

    list_usia = ['Semua Usia'] + list(df_kuesioner['Usia '].unique())
    pilihan_usia = st.selectbox("🎯 FILTER UTAMA: Pilih Kelompok Usia Responden", list_usia)

    if pilihan_usia != 'Semua Usia':
        data_kues_filtered = df_kuesioner[df_kuesioner['Usia '] == pilihan_usia]
    else:
        data_kues_filtered = df_kuesioner

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("1. Distribusi Kelompok Usia")
        fig_usia = ana.grafik_usia(data_kues_filtered)
        st.pyplot(fig_usia)

    with col2:
        st.subheader("2. Komposisi Jenis Kelamin")
        fig_gen = ana.grafik_gender(data_kues_filtered)
        st.pyplot(fig_gen)

    st.write("---")
    st.subheader("3. Rata-rata Skor Kepuasan Aspek Utama Aplikasi")
    fig_fitur = ana.grafik_kepuasan_fitur(data_kues_filtered)
    st.pyplot(fig_fitur)

with tab_playstore:
    st.header("Analisis Ulasan Keluhan Pengguna (Play Store)")
    st.subheader("1. Kategori Keluhan Terbanyak (Rating 1 & 2)")
    
    # Memanggil grafik keluhan dari data hasil scraping internet
    fig_ps1 = ana.grafik_keluhan_playstore(df_playstore)
    st.pyplot(fig_ps1)