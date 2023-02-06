"""
Задание 4. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

Пример:
Введите целые числа через пробел: 1 2 3 4
Результат: 2 1 4 3

Введите целые числа через пробел: 1 2 3
Результат: 2 1 3
"""
input_string = input("Введите элементы через пробел: ")
input_array = input_string.split()

new_array = []
i=0

if len(input_array)%2 == 0:
    while i < len(input_array):
        new_array.insert(i,input_array[i+1])
        new_array.insert(i+1, input_array[i])
        i+=2
else:
    new_array.append(input_array[-1])
    while i < len(input_array)-1:
        new_array.insert(i,input_array[i+1])
        new_array.insert(i+1, input_array[i])
        i+=2

print(' '.join(map(str, new_array))) 