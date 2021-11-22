import sys

size = 1000


def create_generator(size):
    print('Start')
    for number in range(size):
        print('--->')
        yield number ** 2


my_obj = create_generator(size)
print(next(my_obj))
print(next(my_obj))
print(next(my_obj))
# print(type(my_obj))










# my_list = [number ** 2 for number in range(size)]
# print('Size: ' + str(sys.getsizeof(my_list)) + ' byte')
#
#
#
# my_generator = (number ** 2 for number in range(size))
#
# for value in my_generator:
#     pass
#
# print()
# print(my_generator)
# print('Size: ' + str(sys.getsizeof(my_generator)) + ' byte')









# my_list = [1, 2, 3]
#
# class MyNumber:
#     def __iter__(self):
#         self.value = 1
#         return self
#
#     def __next__(self):
#         value = self.value
#         if value < 1000:
#             self.value += 1
#             return value
#         else:
#             raise StopIteration
#
#
#
#
# numbers = MyNumber()
# iter_numb = iter(numbers)
#
# for value in iter_numb:
#     print(value)



# print(next(iter_numb))
# print(next(iter_numb))
# print(next(iter_numb))
# print(next(iter_numb))
# print(next(iter_numb))







# for value in my_list:
#     print(value)
#
# iter_list = iter(my_list)
# print(iter_list)  # <list_iterator object at 0x7f04fd5870a0>
# print(type(my_list), type(iter_list))  # <class 'list'> <class 'list_iterator'>
#
# print(next(iter_list))
# print(next(iter_list))
# print(next(iter_list))
# print(next(iter_list))  # StopIteration

