with open('example.txt', mode = 'r') as f:
    text = f.read()
    print(text)

with open('example.txt', mode = 'w') as f:
    text = f.write('Hi!')

with open('example.txt', 'r') as f:
    text2 = f.read()
    print(text2)