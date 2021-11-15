# Set Comprehensions

quote = 'Life, uh, finds a way'
unique_vowels = {i for i in quote if i in 'aeiou'}
print(unique_vowels, type(unique_vowels))

# Dictionary Comprehensions

squares = {i: i * i for i in range(10)}
print(squares, type(squares))

