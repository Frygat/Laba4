import json  # Так как мы работаем с json необходимо импортировать модуль для работы с ним

def task() -> float:
    with open('input.json', 'r') as f:  #открываем данный нам файл и считываем в режиме 'r'(считывание по умолчанию, которое позволяет доставать содержимое из файла без его изменения)
        data = json.load(f) #Десериализуем JSON

    total_sum = sum([item["score"] * item["weight"] for item in data]) #Вычисление суммы для каждого словаря в 'data'

    return round(total_sum, 3)


print(task())






