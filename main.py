import re

# Функція для зчитування першого речення з файлу
def read_first_sentence(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            # Розділяємо текст на речення за допомогою регулярного виразу
            sentences = re.split(r'(?<=[.!?])\s+', text)
            if len(sentences) > 0:
                # Виводимо перше речення
                print("Перше речення:")
                print(sentences[0])
                return sentences[0]
            else:
                print("Файл порожній або не містить речень.")
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print(f"Помилка: {str(e)}")

# Функція для правильного сортування українських слів
def ukrainian_sort_key(word):
    # Створюємо спеціальний ключ для сортування українських слів
    alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    return [alphabet.index(letter) for letter in word.lower()]

def english_sort_key(word):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return [alphabet.index(letter) for letter in word.lower()]

# Функція для виведення відсортованих слів
def print_sorted_words(sentence):
    # Знаходимо всі слова у реченні та видаляємо знаки пунктуації
    words = re.findall(r'\b\w+\b', sentence)
    words = [word for word in words if word.isalpha()]  # Видаляємо слова з неалфавітними символами

    # Розділяємо слова на українські та англійські
    ukrainian_words = sorted([word for word in words if re.match(r'^[а-яїієґ]+$', word, re.I)], key=ukrainian_sort_key)
    english_words = sorted([word for word in words if re.match(r'^[a-z]+$', word, re.I)], key=english_sort_key)

    # Виводимо українські та англійські слова
    if ukrainian_words:
        print("\nУкраїнські слова:")
        print(", ".join(ukrainian_words))
    if english_words:
        print("\nАнглійські слова:")
        print(", ".join(english_words))

    # Виводимо кількість слів у реченні
    print(f"\nКількість слів: {len(words)}")

# Головна функція
def main():
    filename = 'input.txt'
    sentence = read_first_sentence(filename)
    if sentence:
        if len(sentence.split()) > 100:
            print("Речення містить більше 100 слів. Обробку припинено.")
        else:print_sorted_words(sentence)

if __name__ == "__main__":
    main()
