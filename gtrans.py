from first.google_mod import TransLate, LangDetect, CodeLang, LanguageList

print(TransLate("Hello", "en", "uk"))
print(LangDetect("Hello", "all"))
print(CodeLang("Ukrainian"))
print(LanguageList("screen", "Hello"))