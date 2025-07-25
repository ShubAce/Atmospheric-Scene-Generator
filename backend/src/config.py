
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HF_API_TOKEN = os.getenv("HF_TOKEN")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
FREESOUND_API_KEY = os.getenv("FREESOUND_API_KEY")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GENERATED_FILES_DIR = os.path.join(BASE_DIR, "generated_files")

os.makedirs(GENERATED_FILES_DIR, exist_ok=True)