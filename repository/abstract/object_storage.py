from abc import ABC, abstractmethod
class ObjectStorageReopository(ABC):
    @abstractmethod
    def fetch_file(self, file_path:str)-> bytes:
        pass
