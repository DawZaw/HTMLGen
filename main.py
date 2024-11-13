from FileManager import FileManager

file_manager: FileManager = FileManager()


def main() -> None:
    text: str | None = file_manager.read('artykul.txt')
    
    if text:
        file_manager.write(text, 'artykul.html')


if __name__ == "__main__":
    main()