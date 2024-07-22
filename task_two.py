import re
from typing import Callable

# Генератор чисел з тексту

def generator_numbers(text: str):
    # Паттерн для пошуку чисел з десятковою точкою
    pattern = r'\d+.\d+'
    # Пошук підходящих чисел у тексті
    matches = re.findall(pattern, text)
    # Перетворення знайдених чисел у float та повернення як генератора
    for i in matches:
        yield float(i)


# Підрахунок суми чисел з тексту
def sum_profit(text: str, func: Callable):
    num = sum(func(text))
    print(num)
    return num







text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
