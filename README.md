# Generator artykułów HTML z pliku tekstowego

## Opis
Program ten wczytuje plik tekstowy z artykułem, następnie za pomocą API OpenAI zostaje on przekonwertowany do formatu HTML, wraz z sugerowanymi promptami do wygenerowania obrazów w poszczególnych paragrafach. 

## Wymagania
Do użycia tego programu wymagane są biblioteki 
- python-dotenv
- openai

oraz klucz API OpenAI

W celu zainstalowania bibliotek można się posłużyć plikiem requirements.txt
```bash
pip install -r requirements.txt
```
lub ręcznie
```bash
pip install python-dotenv
pip install openai
```

W głównym folderze należy utworzyć plik .env według przykładu poniżej, w którym należy zapisać swój klucz API.
```python
OPENAI_API_KEY=#Miejsce na klucz
```

## Sposób użycia
W celu użycia aplikacji należy uruchomić program wraz z argumentem -f FILENAME, w którym wskazuje się nazwę pliku tekstowego.
```bash
python main.py -f plik.txt
```
Jeżeli plik tekstowy znajduje się w innym folderze niż program, można użyć opcjonalnego argumentu -p PATH i wskazać nową ścieżkę pliku
```bash
python main.py -p D:\folder -f plik.txt
```
W rezultacie zostanie wygenerowany plik artykul.html