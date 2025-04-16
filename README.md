# RespiraScan AI - Deteksi Bakteri ISPA

RespiraScan AI adalah sistem klasifikasi bakteri penyebab Infeksi Saluran Pernapasan Akut (ISPA) menggunakan Convolutional Neural Network (CNN) dengan arsitektur InceptionResNet-V2.

## 🔬 Tentang Proyek

Proyek ini dikembangkan sebagai bagian dari skripsi untuk membantu mengklasifikasikan beberapa jenis bakteri penyebab ISPA melalui analisis gambar mikroskop. Sistem ini menggunakan teknologi AI untuk memberikan hasil klasifikasi yang akurat dan cepat.

### Bakteri yang Dapat Dideteksi:

- Streptococcus pneumoniae
- Staphylococcus aureus
- Mycobacterium tuberculosis
- Corynebacterium diphtheriae
- Pharyngitis

## 🚀 Teknologi yang Digunakan

- **Backend:** Python, Flask
- **Frontend:** HTML, TailwindCSS, JavaScript
- **AI/ML:** TensorFlow, Keras
- **Model:** InceptionResNet-V2
- **Image Processing:** PIL, NumPy

## 📋 Persyaratan Sistem

```bash
Python 3.8 or higher
Flask 2.3.3
TensorFlow 2.13.0
Keras 2.13.1
Pillow 10.0.1
NumPy 1.24.3
```

## 🛠️ Instalasi

1. Clone repositori

```bash
git clone https://github.com/username/RespiraScanAI.git
cd RespiraScanAI
```

2. Buat virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Jalankan aplikasi

```bash
python run.py
```

## 🌐 Penggunaan

1. Buka browser dan akses `http://localhost:5000`
2. Navigasi ke halaman "Mulai"
3. Upload gambar mikroskop bakteri
4. Sistem akan memproses dan menampilkan hasil klasifikasi

## 📚 Fitur

- Klasifikasi 5 jenis bakteri ISPA
- Interface yang user-friendly
- Hasil klasifikasi dengan persentase kepercayaan
- Informasi detail tentang setiap jenis bakteri
- Responsive design untuk berbagai ukuran layar

## 🔧 Struktur Proyek

```
RespiraScanAI/
├── app/
│   ├── static/
│   ├── templates/
│   ├── model/
│   └── application.py
├── requirements.txt
├── run.py
├── vercel.json
└── README.md
```

## 👨‍💻 Pengembang

- **Abdullah Ali** - _Mahasiswa Teknik Informatika_ - Politeknik Negeri Jember

## 🙏 Ucapan Terima Kasih

- Dosen Pembimbing
- Politeknik Negeri Jember
- Kontributor dan Pengembang Library yang Digunakan

## 📞 Kontak

Untuk pertanyaan dan saran, silakan hubungi:

- LinkedIn: [Abdullah Ali](https://linkedin.com/in/abdlhli)
