# Создание списка с помощью цикла

squares = []

for i in range(10):
    squares.append(i * i)
print(squares)

# map

txns = [1.09, 23.54, 234, 4.5, 43.2]
tax_rate = .08

def get_price_with_tax(txn):
    return txn * (1 + tax_rate)

final_prices = list(map(get_price_with_tax, txns))
print(final_prices)

# list comprehensions

squares = [i * i for i in range(0, 101, 5)]
print(squares)

# 2

sentence = 'the rocket came back from mars'

vowels = [i for i in sentence if i in 'aeiou']
print(vowels)

# 3

sentence = 'The rocket, who was named Ted, came back \
from Mars because he missed his friends.'


def is_consonant(letter):
    vowels2 = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels2


consonants = [i for i in sentence if is_consonant(i)]
print(consonants)

# 4

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]
print(prices)



