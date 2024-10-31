import random
import string

def replace_odd_digits_with_random_letter(text):
    result = []
    for c in text:
        if c.isdigit() and int(c) % 2 != 0:
            random_letter = random.choice(string.ascii_letters)
            result.append(random_letter)
        else:
            result.append(c)
    return ''.join(result)

def count_digits(text):
    return sum(c.isdigit() for c in text)

def count_digits_in_file_and_replace_odds(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Рахуємо кількість цифр до зміни
        digit_count_before = count_digits(text)
        
        # Замінюємо непарні числа на випадкові літери
        modified_text = replace_odd_digits_with_random_letter(text)
        
        # Рахуємо кількість цифр після зміни
        digit_count_after = count_digits(modified_text)
        
        # Записуємо змінений текст назад у файл
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(modified_text)
        
        return digit_count_before, digit_count_after
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
        return 0, 0

# Вказати шлях до вашого файлу
file_path = 'text.txt'

digit_count_before, digit_count_after = count_digits_in_file_and_replace_odds(file_path)
print(f"Кількість цифр у файлі до змін: {digit_count_before}")
print(f"Кількість цифр у файлі після змін: {digit_count_after}")
