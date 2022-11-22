with open('folder/20.11.22.txt', 'r') as file:
    cook_book = {}
    _cook_book = {}
    for line in file:
        dish_name = line.strip()
        number_of_ingradients = int(file.readline())
        ingradients = []
        for _ in range(number_of_ingradients):
            ingradient = file.readline().strip().split(' | ')
            ingradient_name, quantity, mesure = ingradient
            ingradients.append({"ingradient_name": ingradient_name,
                                'quantity': quantity,
                                'mesure': mesure})
            _cook_book = {dish_name: ingradients}
        cook_book.update(_cook_book)
        file.readline()
# Для построчного вывода
print_cook_book = cook_book
for elem in print_cook_book.items():
    print(f'\n{elem[0]}')
    for el in elem[1]:
        print(el)

print()
print(cook_book)







