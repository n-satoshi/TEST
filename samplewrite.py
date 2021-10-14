file = open('InputText.txt', 'w')

while 1:
    x = input()
    file = open('InputText.txt', 'a')

    if x == '-1':
        break

    file.write(x)
    file.write('\n')

file.close()
