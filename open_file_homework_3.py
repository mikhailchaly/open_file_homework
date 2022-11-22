with open('folder/1.txt', 'r') as _file_1:
    _text_1 = _file_1.readlines()
with open('folder/2.txt', 'r') as _file_2:
    _text_2 = _file_2.readlines()
with open('folder/3.txt', 'r') as _file_3:
    _text_3 = _file_3.readlines()
    my_dict = {len(_text_1): '1.txt', len(_text_2): '2.txt', len(_text_3): '3.txt'}
    sort_dict = sorted(my_dict.items(), key = lambda x: x[0])
    print(f'\nОтсортируем по количеству строк: {sort_dict}')
    with open('folder/1.txt', 'r') as file_1:
        text_1 = file_1.read()
    with open('folder/2.txt', 'r') as file_2:
        text_2 = file_2.read()
    with open('folder/3.txt', 'r') as file_3:
        text_3 = file_3.read()
    with open('folder/total_file.txt', 'w') as total:
        total.write(f'Имя файла - {sort_dict[0][1]}\nколичество строк - {sort_dict[0][0]}\n')
        total.write(f'\n{text_2}\n')
        total.write(f'\nИмя файла - {sort_dict[1][1]}\nколичество строк - {sort_dict[1][0]}\n')
        total.write(f'\n{text_1}\n')
        total.write(f'\nИмя файла - {sort_dict[2][1]}\nколичество строк - {sort_dict[2][0]}\n')
        total.write(f'\n{text_3}\n')
    with open('folder/total_file.txt', 'r') as print_total:
        print(print_total.read())
