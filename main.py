import re
from collections import Counter
import mem_usage_test 
import speed
import validator
import verificator

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

    avg_word_length = round(sum(len(word) for word in words) / len(words), 2)
    longest_word = max(words, key=len)

    return {
        "amount": len(words),
        "unique": len(unique_words),
        "frequency": words_frequency,
        "avg_length": avg_word_length,
        "longest_word": longest_word
    }  
    
if __name__ == "__main__":
    text = ""
    while text != "exit":
        try:
            text = input(
                "exit для завершения программы\n" \
                "-help для инструкции: \n" \
                "-memory для теста затрат памяти: \n" \
                "-speed для теста скорости: \n" \
                "-validate для проверки обработки ошибок: \n" \
                "-verificate для проверки верности рещультата: \n" \
                "Введите текст:\n --> ")
            if text == "-help":
                print("Программа получает на ввод текст и выводит:\n" \
                "1. всего слов\n" \
                "2. всего уникальных слов\n" \
                "3. первые 5 по частоте появления слов\n" \
                "4. самое длинное слово\n" \
                "5. средняя длина всех слов\n" \
                "текст должен быть короче 10000 символов\n" \
                "текст должен быть длинее 0 символов\n" \
                "текст не должен содержать ничего кроме латиницы кирилицы чисел и знаков пунктуации\n" \
                "")
            elif (text == "-memory"):
                mem_usage_test.mem_usage_test()
            elif (text == "-speed"):
                speed.work_speed()
            elif (text == "-validate"):
                validator.validate()
            elif (text == "-verificate"):
                verificator.verificate()
            else:
                res = main(text)
                amount = res["amount"]
                unique = res["unique"]
                frequency = res["frequency"]
                avg = res["avg_length"]
                max = res["longest_word"]
                print(f"всего слов: {amount}\nвсего уникальных слов: {unique}") 
                print(f"{len(frequency)} самых частых слов:")
                for i in frequency:
                    print(f"{i[0]} -- {i[1]}")
                print(f"самое длинное слово {max}")
                print(f"средняя длина слов {avg}")
                print("\n")
                print("\n")

        except (KeyboardInterrupt):
            break
            