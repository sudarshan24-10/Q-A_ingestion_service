import fitz
from usecase.file_parser_usecase.base_parser import ParserStratergy

class PdfParser(ParserStratergy):
    def parse(self, file: bytes) -> str:
        doc = fitz.open(stream=file, filetype="pdf")
        paragraphs = []

        for page in doc:
            blocks = page.get_text("blocks")

            for block in blocks:
                text = block[4].strip()
                if not text:
                    continue

                # Normalize internal newlines inside a block
                text = " ".join(line.strip() for line in text.splitlines())

                paragraphs.append(text)

        return "\n\n".join(paragraphs)
