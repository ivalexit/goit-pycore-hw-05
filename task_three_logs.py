from typing import List, Dict
import sys
import os

def parse_logs_line(line: str) -> Dict[str, str]:
    #парсинг логу та повернення словника
    p = line.split(' ', 2)
    if len(p) >= 3:
        time = f'{p[0]} {p[1]}'
        rest = p[2].split(' ', 1)
        level = rest[0].strip()
        message = rest[1] if len(rest) > 1 else ''
        return {'time': time, 'level': level, 'message': message}
    return {}




def load_logs(file_path: str) -> List[Dict[str, str]]:
    #Завантаження лог, повернення списку
    logs: List[Dict[str, str]] = []
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {file_path} не знайдено.")

    with open(file_path, 'r') as file:
        for line in file:
            p_line = parse_logs_line(line.strip())
            if p_line:
                logs.append(p_line)
    return logs


def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    #Фільтр логів за рівнем
    return [log for log in logs if log['level'].lower() == level.lower()]



def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
#Підрахунок по рівнях
    count: Dict[str, int] = {'INFO': 0, 'ERROR': 0, 'DEBUG': 0,'WARNING': 0}
    for log in logs:
        if log in count:
            count[log] += 1
    return count

def display_logs_counts(counts: Dict[str, int]):
    #Виведення записів у таблицю
    print(f"{'Рівень логування':<17} | {'Кількість':<10}")
    print('-' * 30)
    for level, count in counts.items():
        print(f"{level:<17} | {count:<10}")

def display_filtered_logs(logs: List[Dict[str, str]], level: str):
    #Виведення всіх записів за рівнем
    print(f"\nДані логів для рівня '{level.upper()}':")
    for log in logs:
        print(f"{log['time']} - {log['message']}")

def main():
    name_file = sys.argv[1]
    logs = load_logs(name_file)
    print(logs)







if __name__ == '__main__':
 