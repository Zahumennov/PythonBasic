from datetime import datetime


def append_list_one():
    start = datetime.now()
    lst_one = []
    for i in range(10**4):
        if i % 2 == 0:
            lst_one.append(i)
    print(datetime.now() - start)
    return lst_one


def append_list_two():
    start = datetime.now()
    lst_two = [x for x in range(10**4) if x % 2 == 0]
    print(datetime.now() - start)
    return lst_two


l1 = append_list_one()
l2 = append_list_two()


print()
print()
print()


def timeit(arg):
    print(arg)

    def outer(func):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            print(datetime.now() - start)
            return result
        return wrapper
    return outer


@timeit('name')
def append_list_three(n):
    lst_three = [x for x in range(n) if x % 2 == 0]
    return lst_three


l3 = append_list_three(20)
print(l3)

l4 = timeit(append_list_three)
print(type(l4), l4.__name__)

print()

l4 = timeit('name')(append_list_three)(10)

print()
print('==================================================================================')
print()

l5 = append_list_three
l6 = append_list_three(10)
print(l5)
print(l6)

print()
print('==================================================================================')
print()


#Decorator writing practice


def my_decorator(arg):
    print(arg)

    def out(func):
        def wrapper(*args, **kwargs):
            print("start decorator")
            fun = func(*args, **kwargs)
            print("finish decorator")
            return fun
        return wrapper
    return out


@my_decorator("Privet")
def print_fun(n):
    return print(n)


print_fun("Func in")

