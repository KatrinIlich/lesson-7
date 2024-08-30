#Создание переменной и присвоение значения
my_dict = {"Anton": 1990, "Arseny": 1982, "Serega": 1983, "Dima": 1985}
#Вывод словаря
print("Diсt:", my_dict)
#Вывод одного значения по существующему ключу
print("Existing value:", my_dict["Anton"])
#Вывод одного значения по отсутствующему ключу
print("Not existing value:",my_dict.get("Stas"))
#Добавление произвольных пар
my_dict.update({"Liza": 1992, "Olesya": 1993})
#Удаление одной из пар и вывод значения на экран
print("Deleted valua:", my_dict.pop("Serega"))
#Вывод словаря на экран
print("Modified dictionary:", my_dict)

#Присвоение множества переменной
my_set = {23, 23, "Kate", "Kate", True, True}
#Выведение множества
print("Set:", my_set)
#Добавление двух элементов
my_set.update({"year", "cat"})
#Удаление одного из элементов множества
my_set.remove(23)
#Вывод измененного множества
print("Modified dictonary:", my_set)