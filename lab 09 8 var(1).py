import string

def fill_square(letter, N):
    # Отримуємо алфавіт
    alphabet = string.ascii_uppercase
    # Пошук індексу початкової літери
    start_index = alphabet.index(letter.upper())
    # Створення списку літер, які будуть заповнювати квадрат
    letters = [alphabet[(start_index + i) % len(alphabet)] for i in range(N * 4)]
    
    # Розбиваємо на кортежі по сторонах квадрата
    side1 = tuple(letters[:N])
    side2 = tuple(letters[N:2 * N])
    side3 = tuple(letters[2 * N:3 * N])
    side4 = tuple(letters[3 * N:])
    
    # Виведення кортежів для кожної сторони
    print("Сторона 1:", side1)
    print("Сторона 2:", side2)
    print("Сторона 3:", side3)
    print("Сторона 4:", side4)

# Тестування програми
letter = input("Введіть початкову літеру: ")
N = int(input("Введіть кількість літер на кожній стороні квадрата: "))
fill_square(letter, N)
