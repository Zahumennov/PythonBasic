f = open('example.txt', 'w')

l = [str(i)+str(i-1) for i in range(20)]
for index in l:
    f.write(index + '\n')

f.close()


f = open('example.txt', 'r')
print(f.read())

f.close()