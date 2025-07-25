import os
import uuid
import freesound
from elevenlabs.client import ElevenLabs  
from pydub import AudioSegment
from src.config import ELEVENLABS_API_KEY, FREESOUND_API_KEY, GENERATED_FILES_DIR

elevenlabs_client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

freesound_client = freesound.FreesoundClient()
freesound_client.set_token(FREESOUND_API_KEY, "oauth")


def text_to_speech(text: str) -> str | None:
    if not ELEVENLABS_API_KEY:
        raise ValueError("ELEVENLABS_API_KEY is not set.")
    try:
        audio_stream = elevenlabs_client.text_to_speech.stream(
            text=text,
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2"
        )
        
        filepath = os.path.join(GENERATED_FILES_DIR, f"narrative_{uuid.uuid4()}.mp3")
        with open(filepath, 'wb') as f:
            for chunk in audio_stream:
                f.write(chunk)
        return filepath
    except Exception as e:
        print(f"Error with ElevenLabs API: {e}")
        return None

def search_and_download_sound(query: str) -> str | None:
    if not FREESOUND_API_KEY:
        raise ValueError("FREESOUND_API_KEY is not set.")

    try:
        results = freesound_client.text_search(
            query=query,
            fields="id,name,previews",
            sort="downloads_desc"
        )

        if not results.results:
            print(f"No sound found for query: {query}")
            return None

        sound_to_download = results[0]

        filename = f"sfx_{query.replace(' ', '_')}.mp3"
        filepath = os.path.join(GENERATED_FILES_DIR, filename)
        sound_to_download.retrieve_preview(filepath)

        return filepath
    except Exception as e:
        print(f"Error with Freesound client for query '{query}': {e}")
        return None

def create_soundscape(narrative_path: str, sfx_queries: list) -> str | None:
    try:
        narrative_audio = AudioSegment.from_mp3(narrative_path)
        final_audio = AudioSegment.silent(duration=len(narrative_audio) + 2000)
        final_audio = final_audio.overlay(narrative_audio, position=1000)

        for query in sfx_queries:
            sfx_path = search_and_download_sound(query)
            if sfx_path:
                sfx_audio = AudioSegment.from_mp3(sfx_path)
                final_audio = final_audio.overlay(sfx_audio - 12, loop=True)
                os.remove(sfx_path)

        output_filename = f"vignette_{uuid.uuid4()}.mp3"
        output_path = os.path.join(GENERATED_FILES_DIR, output_filename)
        final_audio.export(output_path, format="mp3")

        os.remove(narrative_path)

        return f"/generated_files/{output_filename}"
    except Exception as e:
        print(f"Error during audio mixing: {e}")
        return None