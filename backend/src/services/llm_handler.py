from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from src.config import GROQ_API_KEY

def get_structured_data(user_text: str)-> dict:
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is not present")
    
    llm = ChatGroq(
        model="Gemma2-9b-It",
        temperature=0.8,
        api_key=GROQ_API_KEY
    )

    system_prompt = """You are an expert AI Art Director. Your job is to analyze the user's text and convert it into a structured JSON object for a multi-sensory experience.

    The JSON object must have these exact keys: "image_prompt", "narrative_text", and "sound_search_queries".

    1.  **image_prompt**: Create a rich, detailed, and artistic prompt for the Stable Diffusion XL image generation model. Include details about style (e.g., 'cinematic photo', 'impressionistic painting'), lighting, composition, and mood.
    2.  **narrative_text**: Write a short, poetic paragraph (2-3 sentences) that evokes the feeling of the scene. This will be used for a voiceover.
    3.  **sound_search_queries**: Provide a JSON array of 3-4 simple, two-word search terms suitable for finding audio clips on Freesound.org. Examples: ["gentle rain", "distant thunder", "crickets chirping"].
    """

    prompt= ChatPromptTemplate([
        ("system", system_prompt),
        ("human", "{user_input}")
    ])

    parser = JsonOutputParser()

    chain = prompt | llm | parser

    try:
        response = chain.invoke({"user_input": user_text})
        return response
    except Exception as e:
        print(f"An error occurred while invoking LLM chain: {e}")
        return None