Atmospheric Scene Generator<div align="center"><img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white" alt="Python Version"><img src="https://img.shields.io/badge/FastAPI-0.110-blue?logo=fastapi&logoColor=white" alt="FastAPI"><img src="https://img.shields.io/badge/LangChain-blue?logo=langchain" alt="LangChain"><img src="https://img.shields.io/badge/Tailwind_CSS-3-blue?logo=tailwindcss&logoColor=white" alt="Tailwind CSS"></div><br>A web application that transforms textual descriptions of scenes, memories, or moods into multi-sensory vignettes, complete with a generated image, a narrative voiceover, and an ambient soundscape.This project acts as an AI "Art Director," deconstructing user input and orchestrating multiple AI services to create a cohesive audio-visual experience.How It WorksThe application follows a multi-modal AI pipeline:User Input: You provide a descriptive text of a scene or memory (e.g., "A quiet July evening in Kharagpur after a monsoon shower...").LLM Deconstruction (Groq): The text is sent to a Llama 3 model via the Groq API. The LLM analyzes the text and converts it into a structured JSON object containing key visual elements, a poetic narrative, and search queries for sounds.Image Generation (Stable Diffusion): The generated image prompt is sent to the Hugging Face Inference API to create the visual scene.Voiceover Generation (ElevenLabs): The poetic narrative is sent to the ElevenLabs API to generate a high-quality, natural-sounding voiceover.Soundscape Sourcing (Freesound): The sound keywords are used to search and download ambient audio clips from the Freesound API.Audio Assembly (pydub): The backend uses the pydub library to layer the voiceover and sound effects into a single, immersive audio track.Final Presentation: The generated image and final audio track are presented to the user in the web interface.Tech StackCategoryTechnology / ServiceFrontendHTML5, Tailwind CSS, JavaScriptBackendPython 3.9+, FastAPI, UvicornAI/MLLangChain, langchain-groq, pydubAPIsGroq, Hugging Face Inference, ElevenLabs, FreesoundSystemFFmpeg (Required for pydub)Setup and InstallationFollow these steps to get the project running on your local machine.1. PrerequisitesPython 3.9+: Ensure Python is installed and accessible from your terminal.FFmpeg: You must have FFmpeg installed and added to your system's PATH.See the official FFmpeg download page and follow instructions for your operating system. This is required by pydub for audio processing.2. Clone the Repositorygit clone https://github.com/your-username/atmospheric-scene-generator.git
cd atmospheric-scene-generator
3. Set Up the BackendNavigate to the backend directory and create a Python virtual environment.cd backend

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install the required Python packages
pip install -r requirements.txt
4. Configure API KeysYou need to provide your API keys for the external services.In the project's root directory (atmospheric-scene-generator/), find the file .env.example.Rename this file to .env.Open the .env file and paste your API keys:# .env

# Get from https://console.groq.com/
GROQ_API_KEY="gr_..."

# Get from https://huggingface.co/settings/tokens (must have 'write' role)
HF_API_TOKEN="hf_..."

# Get from https://elevenlabs.io/
ELEVENLABS_API_KEY="..."

# Get from https://freesound.org/home/app_credentials/
FREESOUND_API_KEY="..."
How to Run the ApplicationStart the Backend Server:Make sure you are in the backend/ directory with your virtual environment activated. Run the following command:python main.py
The server will start on http://localhost:8000.Access the Frontend:Open your web browser and navigate to:http://localhost:8000You can now use the application!Project Structureatmospheric-scene-generator/
├── backend/
│   ├── src/
│   │   ├── api/endpoints.py      # FastAPI routes
│   │   ├── services/             # Core application logic
│   │   │   ├── llm_handler.py
│   │   │   ├── image_generator.py
│   │   │   └── audio_handler.py
│   │   └── config.py           # Loads API keys
│   ├── main.py                 # Server entry point
│   └── requirements.txt        # Python dependencies
│
├── frontend/
│   ├── index.html              # Main UI (with Tailwind CSS)
│   └── js/main.js              # Frontend JavaScript
│
├── generated_files/            # Temp storage for generated media
├── .env                        # Your secret API keys (ignored by Git)
├── .env.example                # Template for API keys
├── .gitignore
└── README.md                   # This file
AttributionThis project is powered by several fantastic free-tier services. Please support them!Text Generation: GroqImage Generation: Stable Diffusion via Hugging FaceVoice Generation: ElevenLabsSound Effects: Freesound.orgProject status as of Friday, July 25, 2025 - Kharagpur, West Bengal, India.