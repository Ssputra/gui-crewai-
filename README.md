# 🤖 CrewAI Streamlit Dashboard

Selamat datang di repositori **CrewAI Streamlit Dashboard**. Proyek ini menyediakan antarmuka web (Web UI) yang bersih, modern, dan profesional untuk mempermudah operasional agen kecerdasan buatan CrewAI Anda, khususnya bagi lingkungan *self-hosted* di VPS atau server lokal.

## ✨ Fitur Utama

- **Desain Modern**: Antarmuka responsif dan mudah dinavigasi, dibangun di atas teknologi Streamlit.
- **Kredensial Aman**: Memiliki kolom pengisian *API Key* tersendiri bertipe password, sehingga token akses (seperti OpenAI atau Anthropic) Anda tidak akan terekam dalam *source code*.
- **Parameter Instruksi**: Mengizinkan pengguna memasukkan topik utama dan penjelasan detail (prompt) yang langsung diarahkan ke *agent*.
- **Log Di Balik Layar (*Verbose*)**: Memantau perkembangan masing-masing agen secara berurutan dan *real-time* melalui fitur expander.
- **Render Output Markdown**: Hasil akhir pemikiran CrewAI akan dirender otomatis menjadi dokumen visual berformat Markdown yang rapi.
- **Tombol Unduh (Export)**: Mengekspor laporan langsung dari aplikasi menjadi file lokal berektensi `.md`.

## 🚀 Cara Menjalankan

### 1. Persiapan (Prerequisites)
Pastikan sistem operasi Anda (Windows/Linux/Mac) sudah terpasang **Python 3.8+**.

### 2. Kloning Repositori
```bash
git clone https://github.com/Ssputra/gui-crewai-.git
cd gui-crewai-
```

### 3. Instalasi Dependencies
Sangat disarankan untuk menggunakan **Virtual Environment (venv)** agar tidak terjadi bentrok dengan paket sistem (terutama di Linux/VPS seperti Ubuntu/Debian).

Buat dan aktifkan *virtual environment*:
```bash
python3 -m venv venv
source venv/bin/activate  # Untuk Linux/Mac
# venv\Scripts\activate   # Untuk Windows
```

Setelah `venv` aktif (ditandai dengan tulisan `(venv)` di terminal), jalankan perintah instalasi menggunakan pip:
```bash
pip install -r requirements.txt
```

### 4. Eksekusi Aplikasi Web
Jalankan aplikasi dengan perintah khusus Streamlit:
```bash
streamlit run app.py
```
Aplikasi akan aktif dan dapat diakses pada browser melalui alamat `http://localhost:8501`.

## 🔧 Integrasi Dengan Script CrewAI Asli

Secara *default*, file `app.py` menggunakan fungsi simulasi (`run_crewai_task`) untuk merepresentasikan cara kerja antarmuka.

Untuk mengintegrasikannya dengan kode logika CrewAI Anda yang sebenarnya, Anda hanya perlu mengubah blok `run_crewai_task` di dalam `app.py`:
1. *Import* module `Agent`, `Task`, `Crew` dan module pendukung lainnya dari *script* orisinil Anda.
2. Inisialisasi konfigurasi LLM (Large Language Model) menggunakan parameter `api_key` dari pengguna.
3. Kirim nilai parameter `topic` dan `description` sebagai masukan (input) ke agen atau task.
4. Jalankan metode `crew.kickoff()` dan teruskan hasil log serta output akhir ke UI Streamlit.

---
*Dibuat oleh AI Assistant.*