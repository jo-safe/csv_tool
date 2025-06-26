import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True, help='Путь к CSV-файлу')
    parser.add_argument('--where', required=False,
        help='Фильтр вида column=value, пример: price=>500')
    parser.add_argument('--aggregate', required=False,
        help='Агрегация вида column=func, пример: price=avg')

    return parser.parse_args()