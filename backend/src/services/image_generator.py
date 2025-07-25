import requests
import uuid
import os
from src.config import HF_API_TOKEN, GENERATED_FILES_DIR
import os
from huggingface_hub import InferenceClient
from PIL import Image
from io import BytesIO



client = InferenceClient(
    provider="auto",
    api_key=HF_API_TOKEN,
)

def generate_image(prompt: str)-> str| None:
    

    try:
        image = client.text_to_image(
            prompt=prompt,
            model="stabilityai/stable-diffusion-3-medium-diffusers",
        )
        byte_arr = BytesIO()
        image.save(byte_arr, format='PNG') 
        image_bytes = byte_arr.getvalue()
        filename=f"image_{uuid.uuid4()}.jpg"
        filepath=os.path.join(GENERATED_FILES_DIR, filename)

        with open(filepath, "wb") as f:
            f.write(image_bytes)
        
        return f"/generated_files/{filename}"
    
    except Exception as e:
        print(f"Error calling hugging face api: {e}")
        return None