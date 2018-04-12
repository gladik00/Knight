def take():  #читает поле из файла
    field = open('knight.txt', 'r').read().split()
    for i in range(len(field)):
        field[i] = int(field[i])
    n = int(field[0])
    del field[0]
    shaped = []
    for i in range(n):
        a = []
        for j in range(n):
            a.append(field[n * i + j])
        shaped.append(a)
    return shaped


n = len(take())


def place_of_max(ar):  #дает список из двух координат положения коня
    a = 0
    c = [0, 0]
    for i in range(n):
        for j in range(n):
            if ar[i][j] > a:
                c = [i, j]
                a = ar[i][j]
    return c


def poss_list(ar, x, y):  #дает список координат, в которые из данной точки может походить конь
    poss = []
    for i in range(n):
        for j in range(n):
            if ((abs(x - i) == 1 and abs(y - j) == 2) or (abs(x - i) == 2 and abs(y - j) == 1)) and ar[i][j] == 0:
                poss.append([i, j])
    return poss


def full(ar):  #проверяет заполненность списка
    q = 0
    for i in ar:
        for j in i:
            if j == 0:
                q += 1
    if q == 0:
        return True
    else:
        return False


def solve(ar):  #решает задачу с применением рекурсии
    if full(ar):
        return True
    k = place_of_max(ar)
    poss = poss_list(ar, k[0], k[1])
    for i in poss:
        ar[i[0]][i[1]] = ar[place_of_max(ar)[0]][place_of_max(ar)[1]] + 1
        if solve(ar):
            return True
        ar[i[0]][i[1]] = 0
    return False


def output(ar): #красиво оформляет вывод
    for i in ar:
        for j in i:
            print(j, end='\t')
        print('')



lst = take()
possible = solve(lst)
if possible:
    output(lst)
