from random import randint


def bubble_sort(array):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(array)-1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True


lst = [randint(0, 100) for _ in range(15)]
print(lst)
bubble_sort(lst)
print(lst)