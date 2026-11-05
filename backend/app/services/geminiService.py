
import os

from dotenv import load_dotenv
from google import genai
from google.genai import errors

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model_name = os.getenv("GEMINI_MODEL")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is missing from backend/.env")

if not model_name:
    raise RuntimeError("GEMINI_MODEL is missing from backend/.env")

client = genai.Client(api_key=api_key)


class GeminiUnavailableError(Exception):
    """Raised when Gemini is temporarily unavailable."""


def generate_text(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt,
        )
    except errors.APIError as exc:
        if getattr(exc, "code", None) in {429, 500, 502, 503, 504}:
            raise GeminiUnavailableError(
                "Gemini is temporarily unavailable."
            ) from exc
        raise

    if not response.text:
        raise RuntimeError("Model returned an empty response.")

    return response.text
