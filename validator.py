from main import main

def validate():
    text = ""
    print(main(text))

    text = "a" * 100001
    print(main(text))

    text = "🎉☕"
    print(main(text))

if __name__ == "__main__":
    validate()