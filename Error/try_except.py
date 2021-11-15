try:
    k = 1 / 0
except ArithmeticError:
    k = 0

print(k)

f = open('/home/zagum/Study_Programming/PythonBasic/Files/example.txt')
ints = []
try:
    raise Exception('Some shit')
    # for line in f:
    #     ints.append(int(line))
except ValueError:
    print('Это не число!')
except Exception:
    print('WTF')
except (TypeError,ZeroDivisionError):
    print("Неверный ввод")

else:
    print('Все хорошо')
finally:
    f.close()
    print('закрываем')


