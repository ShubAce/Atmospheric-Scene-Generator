Atmospheric Scene Generator 🌆<div align="center"></div><br>A web application that transforms textual descriptions of scenes, memories, or moods into multi-sensory vignettes, complete with a generated image, a narrative voiceover, and an ambient soundscape.This project acts as an AI "Art Director," deconstructing user input and orchestrating multiple AI services to create a cohesive audio-visual experience.<br> FeaturesText-to-Vignette: Converts a simple text description into a full audio-visual scene.AI-Powered Art Direction: Uses a Large Language Model (Llama 3 via Groq) to intelligently generate prompts for other AI services.Multi-Modal Output: Generates a high-resolution image, a natural-sounding voiceover, and a layered ambient soundscape.Modern Web Interface: A clean and responsive UI built with Tailwind CSS.API-First Design: Built on a robust FastAPI backend.🛠️ Tech StackCategoryTechnology / ServiceFrontendHTML5, Tailwind CSS, JavaScriptBackendPython 3.9+, FastAPI, UvicornAI/MLLangChain, langchain-groq, pydubAPIsGroq, Hugging Face Inference, ElevenLabs, FreesoundSystemFFmpeg (Required by pydub)🚀 Getting StartedFollow these steps to get the project running on your local machine.1. PrerequisitesPython 3.9+: Ensure Python is installed and accessible from your terminal.FFmpeg: You must have FFmpeg installed and added to your system's PATH.See the official FFmpeg download page and follow instructions for your operating system. This is required by pydub for audio processing.2. Clone the Repositorygit clone https://github.com/your-username/atmospheric-scene-generator.git
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
▶️ How to RunStart the Backend Server:Make sure you are in the backend/ directory with your virtual environment activated. Run the following command:python main.py
The server will start on http://localhost:8000.Access the Frontend:Open your web browser and navigate to:http://localhost:8000You can now use the application!📁 Project Structureatmospheric-scene-generator/
├── backend/
│   ├── src/
│   │   ├── api/endpoints.py      # FastAPI routes
│   │   ├── services/             # Core application logic
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
📄 LicenseThis project is licensed under the MIT License. See the LICENSE file for details.🙏 AttributionThis project is powered by several fantastic free-tier services. Please support them!Text Generation: GroqImage Generation: Stable Diffusion via Hugging FaceVoice Generation: ElevenLabsSound Effects: Freesound.org<br><div align="center"><em>Project status as of July 25, 2025 - Kharagpur, West Bengal, India.</em></div>