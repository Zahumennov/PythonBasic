from random import random

# def simple_generator(val):
#     while val > 0:
#         val -= 1
#         yield 1
#
#
# gen_iter = simple_generator(5)
# print(next(gen_iter))
#
#
# def generator_function():
#     for i in range(10):
#         yield i
#
#
# for item in generator_function():
#     print(item)
#
# a = generator_function()
# print(next(a))
# print(next(a))

# def fibon(n):
#     a = b = 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
#
#
# for x in fibon(10):
#     print(x)
#
#
#
#
# class RandomIncrease:
#     def __init__(self, quantity):
#         self.qty = quantity
#         self.cur = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.qty > 0:
#             self.cur += random()
#             self.qty -= 1
#             return round(self.cur, 2)
#         else:
#             raise StopIteration
#
#
# iterator = RandomIncrease(5)
# for i in iterator:
#     print(i)

# class Count:
#     """Iterator that counts upward forever."""
#     def __init__(self, start=0):
#         self.num = start
#     def __iter__(self):
#         return self
#     def __next__(self):
#         num = self.num
#         self.num += 1
#         return num




def random_increase(quantity):
    cur = 0
    while quantity > 0:
        cur += random()
        quantity -= 1
        yield round(cur, 2)


generator = random_increase(5)
for i in generator:
    print(i)



def plus_one(num):
    n = 0
    while num > 0:
        num -= 1
        yield n
        n += 1


for i in plus_one(5):
    print(i)