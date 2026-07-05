# Generator Kodu i Komunikacja TCP/IP

Projekt realizujący zadanie z generowania kodu na podstawie szablonów (bez użycia AI). 
Narzędzie wykorzystuje `Jinja2` do wygenerowania klas w Pythonie, które służą do binarnej serializacji danych (za pomocą wbudowanego modułu `struct`). Wygenerowana klasa jest następnie używana do komunikacji sieciowej.

## Struktura działania
1. **Definicja:** Dane zdefiniowane są w `schema/interface.json`.
2. **Generacja:** Skrypt `generator.py` czyta JSON oraz szablon `class_template.jinja2`, tworząc gotowy moduł w folderze `output/`.
3. **Komunikacja:** `client.py` i `server.py` komunikują się po TCP, wymieniając dane czujnika (SensorData) w postaci czystych bajtów.

## Jak uruchomić projekt?

1. Zainstaluj wymaganą bibliotekę:
   `pip install jinja2`
2. Wygeneruj kod (utworzy się plik `generated_model.py`):
   `python generator.py`
3. W jednym oknie terminala uruchom serwer:
   `python server.py`
4. W drugim oknie terminala uruchom klienta, aby wysłać dane:
   `python client.py`