programming_languages = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "JavaScript": "Brendan Eich",
    "C#": "Anders Hejlsberg"
}

for language, developer in programming_languages.items():
    print(f"My favorite programming language is {language}. It was created by {developer}")
programming_languages.__delitem__("Java")

print(programming_languages)
