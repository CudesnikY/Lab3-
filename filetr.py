import json
import os
import re
from first.deep_mod import TransLate, LangDetect, CodeLang

def load_config(config_path: str):
    """Завантажує конфігурацію з файлу."""
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"Помилка завантаження конфігурації: {e}")
        return None

def analyze_text(text: str):
    """Аналізує текст: кількість символів, слів і речень."""
    char_count = len(text)
    word_count = len(text.split())
    sentence_count = len(re.split(r'[.!?]+', text)) - 1
    return char_count, word_count, sentence_count

def read_text_file(file_path: str, char_limit: int, word_limit: int, sentence_limit: int):
    """Читає текст із файлу з обмеженнями на кількість символів, слів і речень."""
    if not os.path.exists(file_path):
        print("Файл не знайдено.")
        return None
    
    with open(file_path, 'r', encoding='utf-8') as file:
        text = ""
        for line in file:
            text += line
            char_count, word_count, sentence_count = analyze_text(text)
            if char_count > char_limit or word_count > word_limit or sentence_count > sentence_limit:
                break
        return text.strip()

def main():
    config = load_config("config.json")
    if not config:
        return
    
    text_file = config["text_file"]
    target_language = config["target_language"]
    output = config["output"]
    char_limit = config["char_limit"]
    word_limit = config["word_limit"]
    sentence_limit = config["sentence_limit"]
    
    # Виведення інформації про файл
    if os.path.exists(text_file):
        file_size = os.path.getsize(text_file)
        print(f"Файл: {text_file}")
        print(f"Розмір файлу: {file_size} байт")
        
        # Читання та аналіз тексту
        text = read_text_file(text_file, char_limit, word_limit, sentence_limit)
        if not text:
            print("Не вдалося зчитати текст з файлу.")
            return

        char_count, word_count, sentence_count = analyze_text(text)
        detected_language = LangDetect(text, "lang")
        print(f"Кількість символів: {char_count}")
        print(f"Кількість слів: {word_count}")
        print(f"Кількість речень: {sentence_count}")
        print(f"Мова тексту: {detected_language}")

        # Переклад тексту
        translation = TransLate(text, scr=detected_language, dest=target_language)
        
        # Вивід перекладу
        if output == "screen":
            print(f"\nМова перекладу: {CodeLang(target_language)}")
            print(f"Перекладений текст:\n{translation}")
        elif output == "file":
            output_file = f"{os.path.splitext(text_file)[0]}_{target_language}.txt"
            try:
                with open(output_file, "w", encoding="utf-8") as file:
                    file.write(translation)
                print("Ok")
            except Exception as e:
                print(f"Помилка запису перекладу в файл: {e}")
    else:
        print("Файл тексту не знайдено.")

if __name__ == "__main__":
    main()