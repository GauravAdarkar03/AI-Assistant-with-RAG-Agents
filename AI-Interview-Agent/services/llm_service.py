from openai import OpenAI
from config import OPENAI_API_KEY, MODEL_NAME

client = OpenAI(api_key=OPENAI_API_KEY)

class LLMService:

    @staticmethod
    def generate(messages):

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=0.4,
            max_tokens=500
        )

        return response