'''
1. Дан список чисел. 
Создать список, в который попадают числа, 
описываемые возрастающую последовательность. 

Пример: [1, 5, 2, 3, 4, 6, 1, 7] 
     => [1, 2, 3] 
    или [1, 7] 
    или [1, 6, 7] и т.д. 

Порядок элементов менять нельзя
'''
# Не понял самого алгоритма, пока что


'''
2. Создать и заполнить файл случайными целыми значениями. 
Выполнить сортировку содержимого файла по возрастанию.
'''
import random
def create_file_random_number(quantity, file_name):
    with open(file_name, 'w') as data:
        for i in range(quantity):
            new_data = str(random.randint(0, 100)) + "\n"
            data.write(new_data)

def print_file_content(file_name):
    print("\nСодержимое файла:")
    data = open(file_name, 'r')
    for line in data:
       print(line)
    data.close()

def sort_number_in_file(file_name):
    with open(file_name, 'r') as data:
        data_from_file = data.readlines()
        list_from_file = list(map(int, data_from_file))
        
    list_from_file.sort()

    with open(file_name, 'w') as data:
        for i in list_from_file:
            data.write(f'{i}\n')


file = 'newFile.txt'

create_file_random_number(5, file)
print_file_content(file)

sort_number_in_file(file)
print_file_content(file)

'''
3. Вот вам файл с тысячей чисел. 
    /HomeWork/1Kints.txt

Задача: найти триплеты и просто выводить их на экран. 
Триплетом называются три числа, которые в сумме дают 0. 
(решение будет долгим, ибо является демонстрационным 
при теме многопоточного программирования).
'''
exit()
path = 'HomeWork/1Kints.txt'

# data = open(path, 'r')
# for line in data:
#     i = line
#     print(f'i {i}')
#     for line in data:
#         j = line
#         print(f'j {j}')
#         for line in data:
#             k = line
#             if i+j+k == 0: print(i, j, k)
# data.close()

with open(path, 'r') as data:
    input_list = data.readlines()
    #input_list.pop()
    list_val = list(map(int, input_list))
count = 0
for i in list_val:
    for j in list_val:
        for k in list_val:
            if(i + j + k == 0):
                print(f'{i} , {j} , {k}')
                count += 1
print(f'Количество триплетов равно {count}')