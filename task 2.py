import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
  with open(INPUT_FILENAME, "r") as f:
    reader = csv.DictReader(f)  # чтение csv.файла, где ключами словарей будут заголовки
    data = list(reader)

    with open(OUTPUT_FILENAME, "w") as f: #Открываю входной файл для записи
        json.dump(data, f, indent=4) #Сериализую data в формат JSON, и делаю отступы в 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
