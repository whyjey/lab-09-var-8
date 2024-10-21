def polygon_sides():
    sides_dict = {}
    
    # Введення кількості сторін
    num_sides = int(input("Введіть кількість сторін багатокутника: "))
    
    # Заповнення словника назвами та довжинами сторін
    for i in range(1, num_sides + 1):
        name = input(f"Введіть назву сторони {i}: ")
        length = float(input(f"Введіть довжину сторони {name}: "))
        sides_dict[name] = length
    
    # 1) Вивести кількість сторін
    print("Кількість сторін:", len(sides_dict))
    
    # 2) Вивести найдовшу сторону
    max_side = max(sides_dict, key=sides_dict.get)
    print(f"Найдовша сторона: {max_side} з довжиною {sides_dict[max_side]}")
    
    # 3) Вивести довжину заданої сторони
    side_name = input("Введіть назву сторони для пошуку її довжини: ")
    if side_name in sides_dict:
        print(f"Довжина сторони {side_name}: {sides_dict[side_name]}")
    else:
        print(f"Сторона {side_name} не знайдена.")
    
    # 4) Вивести суму довжин всіх сторін
    total_length = sum(sides_dict.values())
    print(f"Загальна довжина всіх сторін багатокутника: {total_length}")

# Тестування програми
polygon_sides()
