from functools import reduce

a = ['a', 'b', 'c', 'd', 'e']
b = [1, 2, 3, 4, 5]

res = list(map(lambda x, y: (x, y), a, b))
print(res)

print()

nums = [10, 12, 43, 234, 1, 30, 21, 50, 90, 75, 100, 0]


def some_func(num):
    return num > 40

over_40 = list(filter(some_func, nums))

print(over_40)

words = ['ono', 'two', 'three', 'madam']

polindromes = list(filter(lambda word: word == word[::-1], words))
print(polindromes)


print()

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def custom_sum(a, b):
    return a + b


result = reduce(custom_sum, nums)
result_two = reduce(custom_sum, nums, 10)

print(result, '|', result_two)
