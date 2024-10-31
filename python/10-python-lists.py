n = int(input())

array = []
for _ in range(n):
    opc = input().split(" ")

    match opc[0]:
        case 'insert':
            array.insert(int(opc[1]), int(opc[2]))
        case 'print':
            print(array)
        case 'remove':
            array.remove(int(opc[1]))
        case 'append':
            array.append(int(opc[1]))
        case 'sort':
            array.sort()
        case 'pop':
            array.pop()
        case 'reverse':
            array.reverse()

print(array)