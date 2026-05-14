from main import main
def verificate():
    text = "Green Blue Blue Red"
    expected_amount = 4
    expected_unique = 3
    expected_frequency = {"Blue" : 2, "Green" : 1, "Red" : 1}

    data = main(text)
    a = False
    u = False
    f = False
    if data["amount"] == expected_amount:
        a = True
    if data["unique"] == expected_unique:
        u = True
    frequency_dict = dict(data["frequency"])
    r = frequency_dict["red"] == expected_frequency["Red"]
    g = frequency_dict["green"] == expected_frequency["Green"]
    b = frequency_dict["blue"] == expected_frequency["Blue"]
    if r and g and b:
        f = True

    print(a, u, f)

if __name__ == "__main__":
    verificate()