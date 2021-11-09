
# Ex #1
import copy

result_a = [90, 85, 82]
result_b = copy.deepcopy(result_a)
result_c = copy.copy(result_a)
result_d = result_a
result_c[0] = 1

print(result_a, id(result_a))
print(result_b, id(result_b))
print(result_c, id(result_c))
print(result_d, id(result_d))

test_1 = [1, 2, 3, [1, 2, 3]]
test_copy = copy.copy(test_1)
print(test_1, '|---|', test_copy)
test_copy[3].append(4)
print(test_1, '|---|', test_copy)
test_copy.append(4)
print(test_1, '|---|', test_copy)

