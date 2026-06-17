import main

def validate():
    text = ""
    a, b = main.main(text)
    if not a:
        print("Ошибка пустого текста успешно обработана")
    else:
        print("Ошибка пустого текста не обработана")

    text = "a" * 100001
    a, b = main.main(text)
    if not a:
        print("Ошибка слишком большого текста успешно обработана")
    else:
        print("Ошибка слишком большого текста не обработана")

    text = "🎉☕"
    a, b = main.main(text)
    if not a:
        print("Ошибка недопустимых символов в тексте успешно обработана")
    else:
        print("Ошибка недопустимых символов в тексте не обработана")

if __name__ == "__main__":
    validate()