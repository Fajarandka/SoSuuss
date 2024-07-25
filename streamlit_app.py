import streamlit as st
import numpy as np
import pandas as pd

# Mengatur tema Streamlit dengan dominasi warna ungu sangat gelap
st.set_page_config(
    page_title="Spektrofotometer UV-Vis",
    page_icon="🌟",
    layout="centered",
    initial_sidebar_state="auto"
)

# Custom CSS untuk mengatur warna dan tampilan
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1a001f; /* Warna ungu sangat gelap */
        color: #FFFFFF; /* Warna teks putih */
    }
    .stTitle {
        color: #FFFFFF; /* Warna judul putih */
    }
    .stButton button {
        background-color: #000000; /* Warna tombol hitam */
        color: #FFFFFF; /* Warna teks tombol putih */
    }
    .stSelectbox .st-cj {
        color: #FFFFFF; /* Warna teks selectbox putih */
    }
    .stSelectbox .st-br {
        background-color: transparent; /* Warna background selectbox transparan */
    }
    .stTextArea textarea {
        background-color: #000000; /* Warna background textarea hitam */
        color: #FFFFFF; /* Warna teks textarea putih */
    }
    .jawaban {
        color: #FFD700; /* Warna jawaban signifikan kuning emas */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Judul aplikasi
st.title("🌀 Penentuan Panjang Gelombang dan Kurva Kalibrasi pada Spektrofotometer UV-Vis 🌟")

# Opsi
opsi = st.selectbox("Pilih opsi:", ["Tentang Kami", "Informasi Lanjut", "Penentuan Panjang Gelombang", "Penentuan Kurva Kalibrasi"])

# Konten opsi pertama
if opsi == "Tentang Kami":
    st.write("### Tentang Kami:")
    st.write("Aplikasi ini berguna untuk menentukan panjang gelombang dan kurva kalibrasi pada spektrofotometer UV-Vis.")
    st.write("Aplikasi ini juga merupakan hasil proyek kami dalam mata kuliah yang dijalankan. Kami berterima kasih atas pengertiannya.")
    st.write("### Anggota Kelompok:")
    st.write("1. Fajar Putra Andika")
    st.write("2. Inka Novebi Br Ginting")
    st.write("3. Muhammad Erlan Satriawan")
    st.write("4. Mutya Aziza Rahma")
    st.write("5. Nicorsa Gading Pramodya")
    st.write("6. Abbiyu Dya Wahid S.")

# Konten opsi kedua
if opsi == "Informasi Lanjut":
    st.write("### Informasi Lanjut:")
    st.write("#### Panjang Gelombang")
    st.write("Panjang gelombang adalah jarak antara dua titik pada gelombang yang memiliki fase sama. Dalam spektrofotometer UV-Vis, panjang gelombang digunakan untuk mengidentifikasi warna yang dihasilkan oleh suatu senyawa.")
    st.write("#### Kurva Kalibrasi")
    st.write("Kurva kalibrasi adalah grafik yang menunjukkan hubungan antara absorbansi dan konsentrasi suatu senyawa. Kurva kalibrasi digunakan untuk menentukan konsentrasi suatu senyawa berdasarkan absorbansinya.")
    st.write("##### Kegunaan kurva kalibrasi adalah untuk:")
    st.write("* Menentukan konsentrasi suatu senyawa dalam suatu sampel")
    st.write("* Mengidentifikasi suatu senyawa berdasarkan absorbansinya")
    st.write("* Menentukan kemurnian suatu senyawa")
    st.write("Kurva kalibrasi dapat kita bayangkan seperti gelombang di atas. Sedangkan untuk emotion, kami berharap Anda merasa puas dengan informasi yang kami berikan.")

# Konten opsi ketiga
if opsi == "Penentuan Panjang Gelombang":
    st.write("### Penentuan Panjang Gelombang:")
    warna = st.selectbox("Pilih warna yang diobservasi:", ["Kuning-hijau", "Kuning", "Jingga", "Merah", "Ungu", "Biru", "Hijau-Biru", "Biru-Hijau"])
    if warna == "Kuning-hijau":
        st.write("<div class='jawaban'>Panjang gelombang yang diabsorpsi: 400-435 nm</div>", unsafe_allow_html=True)
    elif warna == "Kuning":
        st.write("<div class='jawaban'>Panjang gelombang yang diabsorpsi: 435-480 nm</div>", unsafe_allow_html=True)
    elif warna == "Jingga":
        st.write("<div class='jawaban'>Panjang gelombang yang diabsorpsi: 480-490 nm</div>", unsafe_allow_html=True)
    elif warna == "Merah":
        st.write("<div class='jawaban'>Panjang gelombang yang diabsorpsi: 490-560 nm</div>", unsafe_allow_html=True)
    elif warna == "Ungu":
        st.write("<div class='jawaban'>Panjang gelombang yang diabsorpsi: 560-580 nm</div>", unsafe_allow_html=True)
    elif warna == "Biru":
        st.write("<div class='jawaban'>Panjang gelombang yang diabsorpsi: 580-595 nm</div>", unsafe_allow_html=True)
    elif warna == "Hijau-Biru":
        st.write("<div class='jawaban'>Panjang gelombang yang diabsorpsi: 595-605 nm</div>", unsafe_allow_html=True)
    elif warna == "Biru-Hijau":
        st.write("<div class='jawaban'>Panjang gelombang yang diabsorpsi: 605-750 nm</div>", unsafe_allow_html=True)

# Konten opsi keempat
if opsi == "Penentuan Kurva Kalibrasi":
    st.write("### Aplikasi Regresi Linier 📉")

    # Input dari pengguna dengan titik sebagai pemisah desimal
    absorbansi = st.text_area("Masukkan nilai absorbansi (pisahkan dengan koma, gunakan titik untuk desimal):")
    konsentrasi = st.text_area("Masukkan nilai konsentrasi (pisahkan dengan koma, gunakan titik untuk desimal):")

    # Tombol untuk menghitung hasil
    if st.button("Hitung"):
        if absorbansi and konsentrasi:
            try:
                # Parsing input dari pengguna
                absorbansi = np.array([float(x) for x in absorbansi.split(',')])
                konsentrasi = np.array([float(x) for x in konsentrasi.split(',')])

                if len(absorbansi) != len(konsentrasi):
                    st.error("Jumlah nilai absorbansi dan konsentrasi harus sama.")
                else:
                    # Membuat DataFrame dari data input
                    data = pd.DataFrame({'Konsentrasi': konsentrasi, 'Absorbansi': absorbansi})
                    st.write("Data:")
                    st.write(data)

                    # Perhitungan regresi linier
                    A = np.vstack([konsentrasi, np.ones(len(konsentrasi))]).T
                    slope, intercept = np.linalg.lstsq(A, absorbansi, rcond=None)[0]

                    # Prediksi dan perhitungan R^2
                    y_pred = slope * konsentrasi + intercept
                    residuals = absorbansi - y_pred
                    ss_res = np.sum(residuals**2)
                    ss_tot = np.sum((absorbansi - np.mean(absorbansi))**2)
                    r2 = 1 - (ss_res / ss_tot)
                    r = np.sqrt(r2)  # Koefisien determinasi

                    # Menampilkan hasil regresi
                    st.write(f"### Hasil Regresi 📊")
                    st.write(f"<div class='jawaban'>Slope (Kemiringan): {slope:.4f}</div>", unsafe_allow_html=True)
                    st.write(f"<div class='jawaban'>Intercept: {intercept:.4f}</div>", unsafe_allow_html=True)
                    st.write(f"<div class='jawaban'>Koefisien Determinasi (R): {r:.4f}</div>", unsafe_allow_html=True)

                    # Data untuk plot
                    plot_data = pd.DataFrame({
                        'Konsentrasi': konsentrasi,
                        'Absorbansi': absorbansi,
                        'Regresi': y_pred
                    })

                    # Plot menggunakan Streamlit
                    st.write("### Plot Data dan Regresi 📈")
                    st.line_chart(plot_data.set_index('Konsentrasi'))

            except ValueError:
                st.error("Masukkan nilai absorbansi dan konsentrasi yang valid (pisahkan dengan koma, gunakan titik untuk desimal).")
        else:
            st.write("Masukkan nilai absorbansi dan konsentrasi untuk melakukan perhitungan.")
