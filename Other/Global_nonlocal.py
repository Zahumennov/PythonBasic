x = 1

def simple_func():
    global x
    x = 50

print(x)
simple_func()
print(x)

a = 50
print()


def one():
    a = 100

    def two():
        a = 200

        def three():
            nonlocal a
            a = 300

        three()
        print(a)
    two()
    print(a)

    
one()
