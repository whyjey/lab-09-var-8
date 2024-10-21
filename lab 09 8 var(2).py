def process_sets():
    A = set([x for x in range(1, 201) if x % 4 == 0])  # Числа, які діляться на 4
    B = set([x for x in range(1, 201) if x % 3 == 0])  # Числа, які діляться на 3
    C = set([x for x in range(1, 201) if x % 5 == 0])  # Числа, які діляться на 5

    # 1) Числа, які діляться на 12
    divisible_by_12 = [x for x in A if x % 12 == 0]
    print("Числа, які діляться на 12:", divisible_by_12)

    # 2) Числа, які діляться на 20 і не діляться на 3
    divisible_by_20_not_3 = [x for x in A if x % 20 == 0 and x % 3 != 0]
    print("Числа, які діляться на 20 і не діляться на 3:", divisible_by_20_not_3)

    # 3) Числа, які діляться на 15 і не діляться на 4
    divisible_by_15_not_4 = [x for x in C if x % 15 == 0 and x % 4 != 0]
    print("Числа, які діляться на 15 і не діляться на 4:", divisible_by_15_not_4)

# Тестування програми
process_sets()
