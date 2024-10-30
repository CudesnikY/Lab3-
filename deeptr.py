from first.deep_mod import TransLate, LangDetect, CodeLang,LanguageList

print(TransLate("Hello", "en", "uk"))
print(LangDetect("Hello", "all"))
print(CodeLang("uk"))
print(LanguageList("screen","Goodbye"))