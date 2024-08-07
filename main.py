def calculate_structure_sum(data_structure):
    def recursive_sum(data):
        total = 0

        if isinstance(data, (list, tuple, set)):
            for item in data:
                total += recursive_sum(item)
        elif isinstance(data, dict):
            for key, value in data.items():
                total += recursive_sum(key)  # Суммируем ключи
                total += recursive_sum(value)  # Суммируем значения
        elif isinstance(data, str):
            total += len(data)  # Суммируем длину строки
        elif isinstance(data, (int, float)):  # Если это число
            total += data

        return total

    return recursive_sum(data_structure)



data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

