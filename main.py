import random
import time

def randomwrite(f, n):
    with open(f, 'w') as file:
        file.seek(0)
        for i in range(0, n):
            file.write(str(random.randint(-1000, 1000)) + ' ')

def bubble_sort(arr):
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return

def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot - 1)
        _quicksort(array, pivot + 1, end)

    return _quicksort(array, begin, end)

def pyzer(file):
    start_time = time.perf_counter()
    f = open(file, 'r').read()
    arr = [float(x) for x in f.split()]
    bubble_sort(arr)
    print(arr)
    print("--- %s секунд пузырем---" % (time.perf_counter() - start_time))

def fast(file):
    start_time = time.perf_counter()
    f = open(file, 'r').read()
    arr = [float(x) for x in f.split()]
    quick_sort(arr)
    print(arr)
    print("--- %s секунд быстрым---" % (time.perf_counter() - start_time))

file = 'inp.txt'

while True:
    print("1. Количество чисел")
    print("2. Пузырем")
    print("3. Быстрым")
    print("0. выйти из программы")
    cmd = input("Выберите пункт: ")

    if cmd == "1":
        randomwrite(file, int(input("Введите количество чисел: ")))
    elif cmd == "2":
        pyzer(file)
    elif cmd == "3":
        fast(file)
    elif cmd == "0":
        exit()
    else:
        print("Вы ввели не правильное значение")