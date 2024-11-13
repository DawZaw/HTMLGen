import os
from argparse import ArgumentParser
from typing import Any

from API import API
from FileManager import FileManager

from settings import SYSTEM_PROMPT


def main(filepath: str, filename: str) -> None:
    openai_api: API = API(SYSTEM_PROMPT)
    file_manager: FileManager = FileManager(filepath)

    article: str | None = file_manager.read(filename)
    if not article:
        return

    response: str | None = openai_api.get_response(article)
    if not response:
        return

    file_manager.write(response, "artykul.html")


if __name__ == "__main__":
    parser: ArgumentParser = ArgumentParser(
        description="Wczytaj plik tekstowy z artykułem, aby przekonwertować go do HTML przy pomocy OpenAI.",
    )
    parser.add_argument(
        "-f",
        "--filename",
        type=str,
        required=True,
        help="Nazwa pliku z artykułem.",
    )
    parser.add_argument(
        "-p",
        "--filepath",
        type=str,
        required=False,
        help="Ścieżka do folderu z artykułem. Domyślnie jest to folder z programem.",
        default=os.path.dirname(__file__),
    )
    args: dict[str, Any] = vars(parser.parse_args())

    filepath: str = args.get("filepath")
    filename: str = args.get("filename")

    main(filepath, filename)
