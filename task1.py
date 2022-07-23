# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

def MakeList():
    print('Введите массив элементов через запятую: ')
    try:
        numbers = [int(number) for number in input().split(', ')]
    except ValueError:
        print('Массив должен состоять из целых чисел, заданных через запятую и пробел.')
        exit()     
    return numbers

def IsInList(num, list):
    if num in list:
        print("Да, такое число есть в массиве")
    else:
        print("Нет, такого числа нет в массиве")

list_of_numbers = MakeList()
number = input('Введите искомое число: ')

try:
    number = int(number)
    IsInList(number, list_of_numbers)
except:
    print('Введите целое число!')