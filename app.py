import streamlit as st
import time

# ==========================================
# Simulasi Eksekusi CrewAI (Placeholder)
# ==========================================
def run_crewai_task(api_key: str, topic: str, description: str):
    """
    Fungsi ini adalah placeholder untuk logika utama CrewAI Anda.
    Di aplikasi aslinya, Anda akan mengimpor Crew, Agents, dan Tasks dari script CrewAI Anda,
    lalu menjalankannya (misal: crew.kickoff()).
    """
    logs = []
    
    # Simulasi proses log (verbose)
    logs.append("[INFO] Memulai inisialisasi CrewAI...")
    time.sleep(1)
    logs.append(f"[INFO] API Key terdeteksi. Otentikasi sukses.")
    logs.append(f"[INFO] Agen 1 (Researcher) ditugaskan untuk topik: '{topic}'.")
    time.sleep(2)
    logs.append("[INFO] Agen 1 mengumpulkan data dan referensi...")
    time.sleep(1)
    logs.append(f"[INFO] Agen 2 (Writer) mulai menyusun deskripsi: '{description}'")
    time.sleep(2)
    logs.append("[SUCCESS] Seluruh tugas CrewAI telah selesai dieksekusi.")
    
    # Simulasi hasil akhir Markdown
    final_output = f"""# Laporan Analisis CrewAI

## 📌 Topik Utama: {topic}

Berdasarkan deskripsi yang Anda berikan (*"{description}"*), agen-agen kami telah merangkum poin-poin berikut:

### 1. Riset Mendalam
Tim agen peneliti telah mengumpulkan berbagai data terbaru terkait topik ini. Proses dilakukan secara komprehensif dari berbagai sumber tepercaya.

### 2. Analisis Konten
- **Kelebihan**: Pendekatan yang efisien dan menghemat waktu.
- **Kekurangan**: Membutuhkan spesifikasi prompt yang detail untuk hasil maksimal.

### 3. Kesimpulan
Proses berhasil dijalankan dan output berhasil digenerate menggunakan format Markdown yang rapi. Anda bisa menggunakan hasil ini untuk keperluan lebih lanjut atau diunduh sebagai file `.md`.

---
*Dihasilkan secara otomatis oleh sistem CrewAI.*
"""
    return logs, final_output

# ==========================================
# Pengaturan Utama Halaman Streamlit
# ==========================================
def main():
    # 1. Header & Deskripsi
    # Konfigurasi halaman agar terlihat modern (layout wide dan ikon robot)
    st.set_page_config(
        page_title="CrewAI Web UI", 
        page_icon="🤖", 
        layout="centered",
        initial_sidebar_state="expanded"
    )
    
    # Menambahkan CSS kustom sederhana untuk mempercantik UI
    st.markdown("""
        <style>
        .main-header {
            font-size: 2.5rem;
            font-weight: 700;
            color: #1E3A8A;
            margin-bottom: 0px;
        }
        .sub-header {
            font-size: 1.1rem;
            color: #6B7280;
            margin-bottom: 20px;
        }
        .result-box {
            background-color: #F3F4F6;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #2563EB;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="main-header">🤖 CrewAI Dashboard</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Panel kontrol modern untuk menjalankan agen AI secara mandiri (self-hosted).</p>', unsafe_allow_html=True)
    st.divider()

    # 2. Input Form di Sidebar
    with st.sidebar:
        st.header("⚙️ Konfigurasi CrewAI")
        st.markdown("Masukkan kredensial dan parameter tugas di bawah ini.")
        
        # Input password/rahasia untuk API Key (aman)
        api_key = st.text_input(
            "🔑 API Key (OpenAI / Anthropic)", 
            type="password", 
            help="Kunci API Anda aman dan tidak disimpan ke dalam database manapun."
        )
        
        st.markdown("---")
        st.subheader("📝 Parameter Tugas")
        
        # Input teks untuk variabel yang dibutuhkan CrewAI
        param_topic = st.text_input(
            "Topik Utama", 
            placeholder="Contoh: Masa Depan AI di 2026"
        )
        param_desc = st.text_area(
            "Deskripsi Detail (Instruksi)", 
            placeholder="Berikan instruksi yang detail untuk agen-agen CrewAI Anda...",
            height=150
        )
        
        # 3. Tombol Eksekusi
        # Tombol eksekusi yang mencolok (type="primary") diletakkan di sidebar bagian bawah
        st.markdown("<br>", unsafe_allow_html=True)
        run_button = st.button("🚀 Jalankan Crew", type="primary", use_container_width=True)

    # 4. Area Konten Utama (Main Dashboard)
    if run_button:
        # Validasi input sederhana sebelum menjalankan CrewAI
        if not api_key:
            st.warning("⚠️ Mohon masukkan API Key terlebih dahulu di menu sidebar.")
        elif not param_topic or not param_desc:
            st.warning("⚠️ Mohon lengkapi Topik Utama dan Deskripsi Detail.")
        else:
            # Tampilkan spinner interaktif selama proses berlangsung
            with st.spinner("⏳ Agen CrewAI sedang bekerja mengumpulkan data dan menyusun laporan. Mohon tunggu..."):
                # Memanggil fungsi CrewAI (pada script Anda yang asli, panggil crew.kickoff() di sini)
                logs, final_result = run_crewai_task(api_key, param_topic, param_desc)
                
            st.success("✅ Eksekusi CrewAI berhasil diselesaikan!")
            
            # Tampilkan log proses di balik layar (Verbose) dalam expander opsional
            with st.expander("🔍 Lihat Log Proses 'Di Balik Layar' (Verbose Logs)"):
                st.code("\n".join(logs), language="plaintext")
            
            # Tampilkan Hasil Akhir dengan Markdown yang rapi
            st.markdown("### 🎯 Hasil Akhir (Final Output)")
            
            # Membungkus markdown dengan container / style khusus (opsional)
            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.markdown(final_result)
            st.markdown('</div><br>', unsafe_allow_html=True)
            
            # 5. Fitur Tambahan: Tombol Unduh (Download Button)
            st.download_button(
                label="📥 Unduh Hasil Akhir (.md)",
                data=final_result,
                file_name=f"crewai_result_{topic.replace(' ', '_').lower()}.md",
                mime="text/markdown",
                use_container_width=True
            )
    else:
        # Tampilan kosong/default sebelum tombol dijalankan
        st.info("👈 Silakan lengkapi konfigurasi di sidebar dan klik **Jalankan Crew** untuk memulai.")

if __name__ == "__main__":
    main()
