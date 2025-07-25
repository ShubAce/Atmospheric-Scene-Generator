# backend/src/api/endpoints.py

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from src.services.llm_handler import get_structured_data
from src.services.image_generator import generate_image
from src.services.audio_handler import text_to_speech, create_soundscape
from src.config import BASE_DIR, GENERATED_FILES_DIR

app = FastAPI()

class SceneRequest(BaseModel):
    text: str

@app.post("/api/v1/generate-scene")
async def generate_scene_endpoint(request: SceneRequest):
    
    print("Received request to generate scene")

    structured_data = get_structured_data(request.text)
    if not structured_data:
        raise HTTPException(status_code=500, detail="Failed to get structured data from LLM.")
    
    image_prompt = structured_data.get("image_prompt")
    image_url = generate_image(image_prompt) if image_prompt else None
    if not image_url:
        raise HTTPException(status_code=500, detail="Failed to generate image.")

    narrative_text = structured_data.get("narrative_text")
    sfx_queries = structured_data.get("sound_search_queries")
    
    narrative_path = text_to_speech(narrative_text) if narrative_text else None
    if not narrative_path:
         raise HTTPException(status_code=500, detail="Failed to generate TTS.")

    audio_url = create_soundscape(narrative_path, sfx_queries) if sfx_queries else None
    if not audio_url:
        raise HTTPException(status_code=500, detail="Failed to create soundscape.")

    return {
        "image_url": image_url,
        "audio_url": audio_url,
        "narrative": narrative_text
    }

app.mount("/generated_files", StaticFiles(directory=GENERATED_FILES_DIR), name="generated_files")
app.mount("/", StaticFiles(directory=f"{BASE_DIR}/frontend", html=True), name="frontend")
