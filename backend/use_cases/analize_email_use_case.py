from backend.use_cases.call_openai_use_case import CallOpenAI
from backend.use_cases.call_gemini_use_case import CallGemini

class AnalizeEmail:
    @staticmethod
    async def analyze_email(text: str) -> dict:
        """
        Analisa o email usando Gemini primeiro. 
        Se falhar, tenta o OpenAI.
        """

        prompt = f"""
            Você é um assistente que analisa emails recebidos.

            1️⃣ Classifique o seguinte email como 'Produtivo' ou 'Improdutivo'.

            - Produtivo: requer ação ou resposta específica.
            - Improdutivo: não exige resposta imediata.

            2️⃣ Se for Produtivo, gere uma resposta automática cordial e breve, com base no que tem descrito no email.  
            3️⃣ Se for Improdutivo, retorne: "Não é necessário uma resposta".

            ⚠️ Retorne **apenas JSON**, sem texto adicional, sem explicações.

            Exemplo de saída correta:
            {{
                "categoria": "Produtivo",
                "resposta": "Obrigado pelo contato, nossa equipe irá analisar e retornar em breve."
            }}

            Email:
            \"\"\"{text}\"\"\"
        """

        try:
            result = await CallGemini.call_gemini(prompt)
            if result:
                return {
                    **result,
                    "sugeridoPor": "Gemini"
                }
        except Exception as e:
            print("Erro ao chamar Gemini:", e)

        try:
            result = await CallOpenAI.call_openAI(prompt)
            if result:
                return {
                    **result,
                    "sugeridoPor": "OpenAI"
                }
        except Exception as e:
            print("Erro ao chamar OpenAI:", e)

        return {
            "categoria": "Indefinido",
            "resposta": "Não conseguimos processar no momento. Nossa equipe irá verificar manualmente.",
            "sugeridoPor": "Fallback"
        }

