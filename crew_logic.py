import os
from crewai import Agent, Task, Crew, Process

def execute_crew(api_key: str, topic: str, description: str) -> str:
    """
    Fungsi utama untuk mengonfigurasi dan menjalankan CrewAI.
    """
    # 1. Setup Environment Variables untuk 9Router
    # CrewAI (lewat LiteLLM) akan otomatis membaca konfigurasi ini
    os.environ["OPENAI_API_BASE"] = "http://ashenra.cloud/v1"
    os.environ["OPENAI_API_KEY"] = api_key or "dummy-key"
    
    model_name = "openai/gpt-3.5-turbo"

    # 2. Definisikan Agents
    researcher = Agent(
        role='Senior Research Analyst',
        goal=f'Melakukan riset mendalam dan mengumpulkan informasi komprehensif mengenai {topic}',
        backstory='Anda adalah analis riset senior di sebuah lembaga riset terkemuka. Keahlian Anda adalah mengidentifikasi tren terbaru dan menganalisis data kompleks.',
        verbose=True,
        allow_delegation=False,
        llm=model_name
    )

    writer = Agent(
        role='Tech Content Strategist',
        goal=f'Membuat konten yang menarik dan mudah dipahami berdasarkan hasil riset mengenai {topic}',
        backstory='Anda adalah Content Strategist yang ahli dalam mengubah riset yang kompleks menjadi artikel atau laporan yang menarik dan profesional.',
        verbose=True,
        allow_delegation=False,
        llm=model_name
    )

    # 3. Definisikan Tasks
    research_task = Task(
        description=f'Lakukan analisis komprehensif mengenai topik berikut: {topic}.\nKonteks/Instruksi Tambahan: {description}.\nIdentifikasi tren utama, kelebihan, dan kekurangannya.',
        expected_output='Laporan riset terperinci yang mencakup temuan utama, tren, dan poin-poin penting dalam bahasa Indonesia.',
        agent=researcher
    )

    writing_task = Task(
        description=f'Gunakan laporan riset yang dihasilkan sebelumnya untuk menulis artikel yang informatif dalam format Markdown mengenai {topic}. Pastikan nada bahasa profesional namun mudah diakses.',
        expected_output='Artikel markdown yang terstruktur dengan baik yang merangkum wawasan utama dari riset. Harus dalam bahasa Indonesia.',
        agent=writer
    )

    # 4. Buat dan Jalankan Crew
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, writing_task],
        verbose=True, # Will print to stdout
        process=Process.sequential
    )

    # Kickoff proses
    result = crew.kickoff()
    return str(result)
