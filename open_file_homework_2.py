dishes = []
for element in input("Введите блюда, через запятую  ").split(','):
    dishes.append(element)
person_count = int(input("Введите количество персон "))

def get_shop_list_by_dishes(dishes, person_count):
    with open('folder/20.11.22.txt', 'r') as file:
        cook_book = {}
        _cook_book = {}
        for line in file:
            dish_name = line.strip()
            number_of_ingradients = int(file.readline())
            _ingradients = {}
            ingradients = {}
            for _ in range(number_of_ingradients):
                ingradient = file.readline().strip().split(' | ')
                ingradient_name, quantity, mesure = ingradient
                _ingradients = {'mesure': mesure,'quantity': int(quantity) * person_count}
                ingradients.update({ingradient_name: _ingradients})
                _cook_book = {dish_name: ingradients}
            cook_book.update(_cook_book)
            file.readline()

    my_dict = {}
    for element in cook_book.items():
        for el in dishes:
            if el in element[0]:
                my_dict = dict(my_dict, **element[1])

    print(my_dict)
    print()
    for elem in my_dict.items():
        # Для построчного вывода
        print(elem)

get_shop_list_by_dishes(dishes, person_count)
