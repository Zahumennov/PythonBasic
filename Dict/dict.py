
my_dict = {}
print(my_dict, type(my_dict))

my_dict_one = {'a': 1, 'b': "2"}
print(my_dict_one, type(my_dict_one))

my_dict_two = dict(one=1, two='2')
print(my_dict_two, type(my_dict_two))

my_dict_three = dict.fromkeys(['a', 'b'], 100)
print(my_dict_three)

my_dict_four = {a: a ** 2 for a in range(7)}
print(my_dict_four, type(my_dict_four), id(my_dict_four))
print(my_dict_four[2])

my_dict_four[4] = 500
print(my_dict_four, type(my_dict_four), id(my_dict_four))

my_dict_four[7] = 'Hey!'
print(my_dict_four, type(my_dict_four), id(my_dict_four))
print()

my_dict_five = my_dict_four
my_dict_six = my_dict_four.copy()
print(my_dict_five, type(my_dict_five), id(my_dict_five))
print(my_dict_six, type(my_dict_six), id(my_dict_six))

my_dict_four.clear()
print(my_dict_four, type(my_dict_four), id(my_dict_four))
print()

print(my_dict_six.get(7))
print(my_dict_six.get(8))
print()

print(my_dict_five.items())
print(dir())