from usecase.file_parser_usecase.pdf_parser import PdfParser
from usecase.file_parser_usecase.base_parser import ParserStratergy
class ParserFactory:
    def __init__(self, file_extension: str):
        self.file_extension = file_extension
        self.parser = {
            "pdf": PdfParser(),
            # "docx": DocxParser(),
            # "txt": TxtParser()
        }
    
    def get_parser(self) ->ParserStratergy | None:
        return self.parser.get(self.file_extension.lower(), None) 
        