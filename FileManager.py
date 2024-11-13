import os

class FileManager:
    path: str

    
    def __init__(self, path: str = os.path.dirname(__file__)) -> None:
        """Domyślną ścieżką jest folder z tym plikiem."""
        self.path = path
        
    def read(self, filename:str) -> str | None:
        filepath: str = self.path + rf"\{filename}"
        
        try: 
            with open(filepath, "r", encoding="UTF-8") as file:
                return file.read()
        except FileNotFoundError:
            print(f"Plik o nazwie '{filename}' nie został znaleziony.")
            return None
        
    def write(self, text: str, filename: str) -> None:
        filepath: str = self.path + rf"\{filename}"
        
        with open(filepath, "w", encoding="UTF-8") as file:
            file.write(text)