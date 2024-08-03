# Projekt Chatbot i Gra Edukacyjna

Ten projekt to aplikacja internetowa, która oferuje platformę edukacyjną, mającą na celu zwiększenie świadomości na temat zmian klimatycznych. Zawiera chatbota zasilanego przez GPT-2, edukacyjną grę quizową oraz strony informacyjne o zmianach klimatu.

## Funkcje

- **Chatbot**: Agent konwersacyjny korzystający z modelu GPT-2 do generowania odpowiedzi. Obsługuje rozmowy w języku polskim dzięki tłumaczeniu wejścia i wyjścia za pomocą Google Translate.
- **Gra Edukacyjna**: Interaktywny quiz, który sprawdza i poszerza wiedzę na temat zmian klimatycznych poprzez pytania wielokrotnego wyboru.
- **Strony Informacyjne**: Zawiera strony z informacjami i zasobami dotyczącymi zmian klimatycznych, mające na celu edukację użytkowników.

## Stos Technologiczny

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Uczenie Maszynowe**: Transformers (Hugging Face) dla modelu GPT-2
- **Tłumaczenie**: Googletrans do tłumaczenia

## Wymagania

- Python 3.7 lub nowszy
- Flask
- PyTorch
- Biblioteka Transformers od Hugging Face
- Biblioteka googletrans do tłumaczenia

## Instalacja

1. **Sklonuj repozytorium**:
    ```bash
    git clone https://github.com/twoja-nazwa-użytkownika/twoje-repo.git
    cd twoje-repo
    ```

2. **Utwórz wirtualne środowisko** (opcjonalnie, ale zalecane):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Na Windows użyj `venv\Scripts\activate`
    ```

3. **Zainstaluj wymagane pakiety**:
    ```bash
    pip install flask, transformers, googletrans. torch
    ```

4. **Uruchom aplikację**:
    ```bash
    python main.py
    ```

   Aplikacja będzie dostępna pod adresem `http://localhost:5001`.

## Podziękowania

- Projekt korzysta z biblioteki [Transformers](https://github.com/huggingface/transformers) od Hugging Face.
- Tłumaczenie realizowane jest za pomocą biblioteki [Googletrans](https://github.com/ssut/py-googletrans).


