# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# Пример:

# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

def MakeList():
    print('Введите массив строк в кавычках через запятую: ')
    list = [str for str in input().split(', ')]
    return list

def SearchStr(str, list):
    second = 0
    pos = -1
    for i in range(len(list)):
        if list[i] == str:
            second += 1
            if second == 2:
                pos = i
                break
    return pos

list_of_str = MakeList()
search = input('Введите искомую строку в кавычках: ')
position = SearchStr(search, list_of_str)
print(position)