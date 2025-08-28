import json
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
clientOpenAI = AsyncOpenAI(api_key=OPENAI_API_KEY)

class CallOpenAI:
    @staticmethod
    async def call_openAI(prompt: str) -> dict:
        try:
            response = await clientOpenAI.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=300
            )
            content = response.choices[0].message.content.strip()
            return json.loads(content)

        except Exception as e:
            print("Erro OpenAI:", e)
            return {
                "categoria": "Indefinido",
                "resposta": "Não conseguimos processar no momento. Nossa equipe irá verificar manualmente.",
                "sugeridoPor": "Fallback"
            }
