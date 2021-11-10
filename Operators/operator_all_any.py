a = [1, 2, 3, 4, 5, []]
b = ['a', True, 2, 1.2, [1, 2, []]]
c = ['a', True, 2, False]
print(all(a), all(b), all(c))

a2 = [1, [], [], []]
b2 = []
c2 = [True, False, False, False, False]
print(any(a2), any(b2), any(c2))
