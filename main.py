import re

def extract_letters(input_string):
    # Используем регулярное выражение для извлечения всех букв из строки
    letters = re.findall(r'[a-zA-Z]', input_string)
    return ''.join(letters)

if __name__ == "__main__":
    user_input = input("Введите строку: ")
    result = extract_letters(user_input)
    print("Буквы в строке:", result)