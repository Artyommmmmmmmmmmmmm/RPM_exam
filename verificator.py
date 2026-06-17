import main

def verificate():
    text = "Green Blue Blue Red"

    expected_amount = 4
    expected_unique = 3
    expected_frequency = {
        "blue": 2,
        "green": 1,
        "red": 1
    }
    expected_avg_length = 4.0
    expected_longest_word = "green"

    data = main.main(text)

    a = data["amount"] == expected_amount
    u = data["unique"] == expected_unique

    frequency_dict = dict(data["frequency"])
    f = all(
        frequency_dict.get(word) == count
        for word, count in expected_frequency.items()
    )

    avg = data["avg_length"] == expected_avg_length
    longest = data["longest_word"] == expected_longest_word

    print(
        "Тест результатов количества пройден"
        if a else
        "Тест результатов количества не пройден"
    )

    print(
        "Тест результатов уникальности пройден"
        if u else
        "Тест результатов уникальности не пройден"
    )

    print(
        "Тест результатов частоты пройден"
        if f else
        "Тест результатов частоты не пройден"
    )

    print(
        "Тест средней длины слова пройден"
        if avg else
        "Тест средней длины слова не пройден"
    )

    print(
        "Тест самого длинного слова пройден"
        if longest else
        "Тест самого длинного слова не пройден"
    )


if __name__ == "__main__":
    verificate()