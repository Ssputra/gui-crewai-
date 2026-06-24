# pyrefly: ignore [missing-import]
import streamlit as st
import time
import io
from contextlib import redirect_stdout
from crew_logic import execute_crew

# ==========================================
# Eksekusi CrewAI (Asli dengan 9Router)
# ==========================================
def run_crewai_task(api_key: str, topic: str, description: str):
    """
    Fungsi untuk menjalankan logika CrewAI dan menangkap log verbose.
    """
    log_capture = io.StringIO()
    status = "SUCCESS"
    
    # Menangkap print out dari CrewAI ke dalam string
    with redirect_stdout(log_capture):
        try:
            print(f"[INFO] Memulai eksekusi CrewAI untuk topik: '{topic}'")
            final_output = execute_crew(api_key, topic, description)
            print("[SUCCESS] Seluruh tugas CrewAI telah selesai dieksekusi.")
        except Exception as e:
            print(f"[ERROR] Terjadi kesalahan: {str(e)}")
            final_output = f"### Terjadi Kesalahan\n\n```\n{str(e)}\n```"
            status = "ERROR"
            
    # Ambil log yang ditangkap, pecah jadi list berdasarkan baris baru
    logs = log_capture.getvalue().split('\n')
    # Filter baris kosong agar UI lebih rapi
    logs = [log for log in logs if log.strip() != '']
    
    return logs, final_output, status

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
            with st.spinner("⏳ Agen CrewAI sedang bekerja mengumpulkan data dan menyusun laporan. Mohon tunggu (proses ini bisa memakan waktu beberapa menit)..."):
                # Memanggil fungsi CrewAI asli
                logs, final_result, status = run_crewai_task(api_key, param_topic, param_desc)
                
            if status == "SUCCESS":
                st.success("✅ Eksekusi CrewAI berhasil diselesaikan!")
            else:
                st.error("❌ Eksekusi CrewAI gagal.")
            
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
                file_name=f"crewai_result_{param_topic.replace(' ', '_').lower()}.md",
                mime="text/markdown",
                use_container_width=True
            )
    else:
        # Tampilan kosong/default sebelum tombol dijalankan
        st.info("👈 Silakan lengkapi konfigurasi di sidebar dan klik **Jalankan Crew** untuk memulai.")

if __name__ == "__main__":
    main()
