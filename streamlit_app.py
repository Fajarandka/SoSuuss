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

# Tambahkan CSS untuk latar belakang gambar dan teks hitam, termasuk header
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1693237476029-f8469bb756a2?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: cover;
}
[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}
[data-testid="stSidebar"] {
    background: rgba(255, 255, 255, 0.2);  /* Transparan dengan efek blur */
    backdrop-filter: blur(5px);  /* Efek blur */
}
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3,
[data-testid="stSidebar"] p, [data-testid="stSidebar"] li {
    color: white; /* Set warna font sidebar menjadi putih */
}
.stMarkdown {
    color: white; /* Set warna teks markdown menjadi putih */
}
.stNumberInput div {
    color: white;  /* Mengubah warna teks input menjadi putih */
}
h2 {
    color: white; /* Set warna h2 menjadi putih */
    border-bottom: 4px solid white; /* Ubah garis bawah menjadi putih */
}
.output {
    color: yellow; /* Set warna output menjadi kuning */
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Judul aplikasi
st.title("🌀 Penentuan Panjang Gelombang dan Kurva Kalibrasi pada Spektrofotometer UV-Vis 🌟")

# Opsi di sidebar
opsi = st.sidebar.selectbox("Pilih opsi:", ["Tentang Kami", "Informasi Lanjut", "Penentuan Panjang Gelombang", "Penentuan Kurva Kalibrasi"])

# Konten opsi pertama
if opsi == "Tentang Kami":
    st.write("### Tentang Kami:")
    st.write("Aplikasi ini berguna untuk menentukan panjang gelombang dan kurva kalibrasi pada spektrofotometer UV-Vis.")
    st.write("Aplikasi ini juga merupakan hasil proyek kami dalam mata kuliah yang dijalankan. Kami berterima kasih atas pengertiannya.")
    
    # Tambahkan gambar sebelum anggota kelompok
    st.image("WhatsApp Image 2024-07-26 at 10.00.33_7cba7d76.jpg", caption="Gambar Anggota Kelompok", use_column_width=True)
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
    
    # Tambahkan gambar sebelum penjelasan panjang gelombang
    st.image("Gelombang Cahaya Tampak.jpg", caption="Gambar untuk Panjang Gelombang", use_column_width=True)
    st.write("#### Panjang Gelombang")
    st.write("Panjang gelombang adalah jarak antara dua titik pada gelombang yang memiliki fase sama. Dalam spektrofotometer UV-Vis, panjang gelombang digunakan untuk mengidentifikasi warna yang dihasilkan oleh suatu senyawa.")

    # Tambahkan gambar sebelum penjelasan kurva kalibrasi
    st.image("Gambar-1-Kurva-Kalibrasi-untuk-posforus-Jika-dilihat-dari-persamaan-regresi-diperoleh-y.png", caption="Gambar untuk Kurva Kalibrasi", use_column_width=True)
    st.write("#### Kurva Kalibrasi")
    st.write("Kurva kalibrasi adalah grafik yang menunjukkan hubungan antara absorbansi dan konsentrasi suatu senyawa. Kurva kalibrasi digunakan untuk menentukan konsentrasi suatu senyawa berdasarkan absorbansinya.")
    st.write("##### Kegunaan kurva kalibrasi adalah untuk:")
    st.write("* Menentukan konsentrasi suatu senyawa dalam suatu sampel")
    st.write("* Mengidentifikasi suatu senyawa berdasarkan absorbansinya")
    st.write("* Menentukan kemurnian suatu senyawa")
    st.write("Kurva kalibrasi dapat kita bayangkan seperti gelombang di atas. Sedangkan untuk emotion, kami berharap Anda merasa puas dengan informasi yang kami berikan.")

# Konten opsi ketiga
if opsi == "Penentuan Panjang Gelombang":
    # Tambahkan gambar sebelum penentuan panjang gelombang
    st.image("1_pAYmNWMpF6-E2Y-txF_ZkQ.jpeg", caption="Gambar untuk Penentuan Panjang Gelombang", use_column_width=True)
    
    st.write("### Penentuan Panjang Gelombang:")
    warna = st.selectbox("Pilih warna yang diobservasi:", ["Kuning-hijau", "Kuning", "Jingga", "Merah", "Ungu", "Biru", "Hijau-Biru", "Biru-Hijau"])
    if warna == "Kuning-hijau":
        st.write("<div class='output'>Panjang gelombang yang diabsorpsi: 400-435 nm</div>", unsafe_allow_html=True)
    elif warna == "Kuning":
        st.write("<div class='output'>Panjang gelombang yang diabsorpsi: 435-480 nm</div>", unsafe_allow_html=True)
    elif warna == "Jingga":
        st.write("<div class='output'>Panjang gelombang yang diabsorpsi: 480-490 nm</div>", unsafe_allow_html=True)
    elif warna == "Merah":
        st.write("<div class='output'>Panjang gelombang yang diabsorpsi: 490-560 nm</div>", unsafe_allow_html=True)
    elif warna == "Ungu":
        st.write("<div class='output'>Panjang gelombang yang diabsorpsi: 560-580 nm</div>", unsafe_allow_html=True)
    elif warna == "Biru":
        st.write("<div class='output'>Panjang gelombang yang diabsorpsi: 580-595 nm</div>", unsafe_allow_html=True)
    elif warna == "Hijau-Biru":
        st.write("<div class='output'>Panjang gelombang yang diabsorpsi: 595-605 nm</div>", unsafe_allow_html=True)
    elif warna == "Biru-Hijau":
        st.write("<div class='output'>Panjang gelombang yang diabsorpsi: 605-750 nm</div>", unsafe_allow_html=True)

# Konten opsi keempat
if opsi == "Penentuan Kurva Kalibrasi":
    st.write("### Aplikasi Regresi Linier 📉")

    # Input dari pengguna untuk menentukan jumlah konsentrasi standar
    num_samples = st.number_input("Masukkan jumlah konsentrasi standar yang diukur:", min_value=1, max_value=100, value=5)

    # Input dari pengguna dalam bentuk tabel untuk kurva kalibrasi
    st.write("Masukkan nilai absorbansi dan konsentrasi dalam tabel di bawah ini (gunakan titik untuk desimal):")
    data_input = st.data_editor(
        pd.DataFrame({"Konsentrasi (ppm)": [0.0] * num_samples, "Absorbansi": [0.0] * num_samples}),
        num_rows="dynamic"
    )

    if st.button("Hitung"):
        if not data_input.empty:
            try:
                # Mengambil data dari tabel
                konsentrasi = data_input["Konsentrasi (ppm)"].values
                absorbansi = data_input["Absorbansi"].values

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
                    r = np.sqrt(r2)  # Koefisien korelasi

                    # Menampilkan hasil regresi
                    st.write(f"### Hasil Regresi 📊")
                    st.write(f"<div class='output'>Slope (Kemiringan): {slope:.4f}</div>", unsafe_allow_html=True)
                    st.write(f"<div class='output'>Intercept: {intercept:.4f}</div>", unsafe_allow_html=True)
                    st.write(f"<div class='output'>Koefisien Korelasi (r): {r:.4f}</div>", unsafe_allow_html=True)
                    st.write(f"<div class='output'>Koefisien Determinasi (R²): {r2:.4f}</div>", unsafe_allow_html=True)
                    st.write(f"<div class='output'>Persamaan Regresi: y = {intercept:.4f} + {slope:.4f}x</div>", unsafe_allow_html=True)

                    # Data untuk plot
                    plot_data = pd.DataFrame({
                        'Konsentrasi': konsentrasi,
                        'Absorbansi': absorbansi,
                        'Regresi': y_pred
                    })

                    # Plot menggunakan Streamlit
                    st.write("### Plot Data dan Regresi 📈")
                    chart = st.line_chart(plot_data.set_index('Konsentrasi'))

                    # Tambahkan keterangan pada plot
                    st.write("### Keterangan Plot")
                    st.write("Sumbu X: Konsentrasi (ppm)")
                    st.write("Sumbu Y: Absorbansi")
            except ValueError:
                st.error("Masukkan nilai absorbansi dan konsentrasi yang valid (gunakan titik untuk desimal).")
        else:
            st.error("Silakan masukkan data dalam tabel.")
