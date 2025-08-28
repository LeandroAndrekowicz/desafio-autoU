import pdfplumber
import os

class ReadFileContent:
    def read_file_content(filename: str, content: bytes) -> str:
        """Lê .txt ou .pdf e retorna string"""
        if filename.endswith(".txt"):
            return content.decode("utf-8", errors="ignore")

        if filename.endswith(".pdf"):
            temp_file = "temp.pdf"
            with open(temp_file, "wb") as f:
                f.write(content)
            text = ""
            with pdfplumber.open(temp_file) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
            os.remove(temp_file)
            return text

        return ""