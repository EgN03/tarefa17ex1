n = int(input("numero"))
i = n
j = n
while i > 0:
    j = 0
    while j < i:
        print(j, end=' ')
        j +=1
    print(' ')
    i -= 1
