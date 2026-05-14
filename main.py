import re
from collections import Counter

def main(text: str):

    if re.search(r'[^\x00-\x7F\u0400-\u04FF\s]', text):
        return False, "Текст содержит недопустимые символы"
    
    if len(text) > 100000:
        return False, "Текст содержит более 100000 символов"
    
    if len(text) < 1:
        return False, "Текст пуст"

    
    
    words = re.findall(r'\b\w+\b', text.lower())
    unique_words = set(words)
    words_frequency = Counter(words).most_common(5)

    return {"amount":len(words), "unique":len(unique_words), "frequency":words_frequency}

    
if __name__ == "__main__":
    text = ""
    while text != "exit":
        text = input(
            "exit для завершения программы\n" \
            "-help для инструкции: \n"
            "Введите текст:\n --> ")
        if text == "-help":
            print("Программа получает на ввод текст и выводит:\n" \
            "1. всего слов\n" \
            "2. всего уникальных слов\n" \
            "3. первые 5 по частоте появления слов\n" \
            "текст должен быть короче 10000 символов\n" \
            "текст должен быть длинее 0 символов\n" \
            "текст не должен содержать ничего кроме латиницы кирилицы чисел и знаков пунктуации\n" \
            "")
        else:
            print(main(text))