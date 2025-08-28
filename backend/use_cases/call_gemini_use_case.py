from google import genai
import json
import asyncio

clientGemini = genai.Client()

class CallGemini:
    @staticmethod
    async def call_gemini(prompt: str) -> dict:
        """
            Chama o modelo Gemini de forma não bloqueante (async) para FastAPI.
            Retorna um dicionário com categoria e resposta.
        """
        def sync_call():
            response = clientGemini.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )
            text = response.candidates[0].content.parts[0].text
            text = text.strip().replace("```json", "").replace("```", "").strip()
            return json.loads(text)

        try:
            return await asyncio.to_thread(sync_call)

        except Exception as e:
            print("Erro Gemini:", e)
            return {
                "categoria": "Indefinido",
                "resposta": "Não conseguimos processar no momento. Nossa equipe irá verificar manualmente.",
                "sugeridoPor": "Fallback"
            }