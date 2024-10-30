from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
from deep_translator.constants import GOOGLE_LANGUAGES_TO_CODES

DetectorFactory.seed = 0

def TransLate(text: str, scr: str, dest: str) -> str:
    """Перекладає текст на задану мову."""
    try:
        translator = GoogleTranslator(source=scr, target=dest)
        return translator.translate(text)
    except Exception as e:
        return f"Помилка перекладу: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    """Визначає мову та коефіцієнт довіри."""
    try:
        lang = detect(text)
        confidence = 1.0  # Бібліотека langdetect не надає коефіцієнта довіри
        if set == "lang":
            return lang
        elif set == "confidence":
            return str(confidence)
        return f"{lang}, {confidence}"
    except LangDetectException as e:
        return f"Помилка визначення мови: {e}"

def CodeLang(lang: str) -> str:
    """Перетворює код або назву мови."""
    lang = lang.lower()
    if lang in GOOGLE_LANGUAGES_TO_CODES:
        return GOOGLE_LANGUAGES_TO_CODES[lang]
    elif lang in GOOGLE_LANGUAGES_TO_CODES.values():
        return {v: k for k, v in GOOGLE_LANGUAGES_TO_CODES.items()}.get(lang, "Мова не знайдена")
    return "Мова не знайдена"

def LanguageList(out: str = "screen", text: str = "") -> str:
    """Виводить таблицю мов та кодів з перекладом тексту."""
    try:
        rows = []
        for i, (lang_name, code) in enumerate(GOOGLE_LANGUAGES_TO_CODES.items(), 1):
            translated_text = GoogleTranslator(source='auto', target=code).translate(text) if text else ""
            rows.append(f"{i:<3} {lang_name:<20} {code:<10} {translated_text}")

        # Створюємо таблицю з заголовками
        table = "N   Language             ISO-639 code  Text\n" + "-" * 50 + "\n" + "\n".join(rows)

        if out == "screen":
            print(table)
        elif out == "file":
            with open("language_list.txt", "w", encoding="utf-8") as file:
                file.write(table)
        return "Ok"
    except Exception as e:
        return f"Помилка: {e}"