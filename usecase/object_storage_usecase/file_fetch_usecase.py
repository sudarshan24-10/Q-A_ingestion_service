from repository.abstract.object_storage import ObjectStorageReopository
from usecase.chunking.file_parser_usecase.base_parser import ParserStratergy
from usecase.chunking.file_parser_usecase.file_parser_factory import ParserFactory
class FileFetchUsecase:
    def __init__ (self, oject_storage_repository: ObjectStorageReopository) -> None:
        self.object_storage_repository = oject_storage_repository
    
    def execute(self, file_path:str)-> str:
        try:
            data = self.object_storage_repository.fetch_file(file_path)
            file_extension:str = file_path.split(".")[-1]
            parser = ParserFactory(file_extension)
        
            parser_strategy: ParserStratergy | None = parser.get_parser()
            if parser_strategy is None:
                raise Exception(f"No parser found for the file extension: {file_extension}")
            parsed_data:str = parser_strategy.parse(data)
            return parsed_data
        except Exception as e:
            raise e
