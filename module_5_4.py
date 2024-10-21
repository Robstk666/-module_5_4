class House:
    houses_history = []  # Атрибут класса для хранения истории объектов

    def __new__(cls, *args, **kwargs):
        # Получаем название здания из args (по индексу 0)
        name = args[0]
        # Добавляем название в историю
        cls.houses_history.append(name)
        # Вызываем родительский метод __new__, чтобы создать сам объект
        instance = super().__new__(cls)
        return instance

    def __init__(self, name, floors):
        # Инициализация атрибутов объекта
        self.name = name
        self.floors = floors

    def __del__(self):
        # Вывод сообщения при удалении объекта
        print(f"{self.name} снесён, но он останется в истории")

# Тестируем класс
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)  # ['ЖК Эльбрус']

h2 = House('ЖК Акация', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация']

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаляем объекты
del h2  # ЖК Акация снесён, но он останется в истории
del h3  # ЖК Матрёшки снесён, но он останется в истории

print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаление последнего объекта
del h1  # ЖК Эльбрус снесён, но он останется в истории