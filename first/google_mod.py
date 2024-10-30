from googletrans import Translator, LANGUAGES

translator = Translator()

def TransLate(text: str, scr: str, dest: str) -> str:
    """Перекладає текст на задану мову."""
    try:
        result = translator.translate(text, src=scr, dest=dest)
        return result.text
    except Exception as e:
        return f"Помилка перекладу: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    """Визначає мову та коефіцієнт довіри."""
    try:
        detection = translator.detect(text)
        if set == "lang":
            return detection.lang
        elif set == "confidence":
            return detection.confidence
        return f"{detection.lang}, {detection.confidence}"
    except Exception as e:
        return f"Помилка визначення мови: {e}"
    


def CodeLang(lang: str) -> str:
    """Повертає код або назву мови."""
    lang = lang.lower()
    if lang in LANGUAGES:
        return lang
    elif lang in LANGUAGES.values():
        return [code for code, name in LANGUAGES.items() if name == lang][0]
    return "Мова не знайдена"

def LanguageList(out: str = "screen", text: str = "") -> str:
    """Виводить список мов і кодів з перекладом тексту."""
    try:
        rows = []
        for i, (code, lang_name) in enumerate(LANGUAGES.items(), 1):
            translated_text = translator.translate(text, dest=code).text if text else ""
            rows.append(f"{i:<3} {lang_name:<20} {code:<10} {translated_text}")
        table = "N   Language             ISO-639 code  Text\n" + "-"*50 + "\n" + "\n".join(rows)
        
        if out == "screen":
            print(table)
        elif out == "file":
            with open("language_list.txt", "w", encoding="utf-8") as file:
                file.write(table)
        return "Ok"
    except Exception as e:
        return f"Помилка: {e}"