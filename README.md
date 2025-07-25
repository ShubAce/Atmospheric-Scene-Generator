# Atmospheric Scene Generator 🌆

<div align="center">
  <strong>A Multi-Sensory AI Art Director</strong>  
</div>

<br>

A web application that transforms textual descriptions of scenes, memories, or moods into immersive, multi-sensory vignettes. Each experience includes a generated image, a natural-sounding voiceover, and an ambient soundscape — all orchestrated intelligently by AI.

This project acts as an **AI Art Director**, deconstructing user input and coordinating multiple services to craft a cohesive and atmospheric audio-visual narrative.

---

## ✨ Features

- **🎞️ Text-to-Vignette:** Converts a short prompt into a complete multi-modal scene.
- **🧠 AI-Powered Art Direction:** Uses a Large Language Model (Llama 3 via Groq) to generate structured prompts for image, voice, and audio generation.
- **🎧 Multi-Modal Output:** Produces a high-res image, narrative voiceover, and ambient soundscape.
- **🌐 Modern Web Interface:** Clean, responsive UI styled with Tailwind CSS.
- **🧩 API-First Design:** Powered by a modular FastAPI backend.

---

## 🛠️ Tech Stack

| Category     | Technology / Service                         |
|--------------|-----------------------------------------------|
| Frontend     | HTML5, Tailwind CSS, JavaScript              |
| Backend      | Python 3.9+, FastAPI, Uvicorn                |
| AI/ML        | LangChain, langchain-groq, pydub             |
| APIs         | Groq, Hugging Face Inference, ElevenLabs, Freesound |
| System Tools | FFmpeg (required by `pydub`)                 |

---

## 🚀 Getting Started

Follow these steps to get the project running locally.

### 1. Prerequisites

- **Python 3.9+**
- **FFmpeg:** Required for audio processing via `pydub`.  
  - Download and install: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
  - Ensure it's added to your system's `PATH`.

---

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/atmospheric-scene-generator.git
cd atmospheric-scene-generator

cd backend

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

mv .env.example .env

# .env

# Get from https://console.groq.com/
GROQ_API_KEY="gr_..."

# Get from https://huggingface.co/settings/tokens
HF_API_TOKEN="hf_..."

# Get from https://elevenlabs.io/
ELEVENLABS_API_KEY="..."

# Get from https://freesound.org/home/app_credentials/
FREESOUND_API_KEY="..."

cd backend
source venv/bin/activate  # or activate your virtual environment
python main.py

http://localhost:8000

atmospheric-scene-generator/
├── backend/
│   ├── src/
│   │   ├── api/endpoints.py      # FastAPI routes
│   │   ├── services/             # Core scene generation logic
│   │   └── config.py             # Loads and manages API keys
│   ├── main.py                   # Entry point for FastAPI server
│   └── requirements.txt          # Python dependencies
│
├── frontend/
│   ├── index.html                # Main UI (styled with Tailwind CSS)
│   └── js/main.js                # Core frontend logic
│
├── generated_files/              # Stores generated media temporarily
├── .env                          # Your API keys (not tracked by Git)
├── .env.example                  # Template file for API keys
├── .gitignore
└── README.md                     # You’re reading it
