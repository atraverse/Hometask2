import string

def read_field(path):
    '''
    read_field
    (str) -> (data)
    що зчитує з файлу filename​ поле та записує його у довільний зручний формат
    data​. Ігрове поле у файлі представлене 10 стрічками, що містять символи *​ —
    частина корабля, яка ще не потонула, X​ — частина корабля, яка уже потонула
    та символ пробіл​ — частина поля, що не містить корабля.
    '''
    lst = []
    with open(path, 'r') as f:
        for line in f:
            lst.append(line)
    lst_1=[]
    for line in lst:
        lst_2=[]
        for i in line:
            if i == '*':
                lst_2.append(1)
            else:
                lst_2.append(0)
        lst_1.append(lst_2)
    for line in lst_1:
        if len(line)>=11:
            for i in range(len(line)-10):
                del line[len(line)-1]
        elif len(line)<10:
            for i in range(10-len(line)):
                line.append(0)
    return (lst_1)


def has_ship():
    '''
    has_ship
    (data, tuple) -> (bool)
    яка на основі зчитаних даних та координат клітинки (наприклад, (J, 1) або (A,
    10)) визначає чи є у даній клітинці корабель.
    '''
    path = "field.txt"
    alp = [i for i in string.ascii_lowercase]
    field = read_field(path)
    lst = []
    for line in field:
        for cells in line:
            if cells ==1:
                ind = line.index(cells)
                lst_1 = [alp[ind], field.index(line)+1]
                line[ind] = 0
                lst.append(lst_1)
    return (lst)


def ship_size(lst_cor):
    '''
    ship_size
    (data, tuple) -> (tuple)
    яка на основі зчитаних даних та координат клітинки (наприклад, (J, 1) або (A,
    10)) визначає розмір корабля, частина якого знаходиться у даній клітинці
    >>>ship_size(['j', 10])
    3
    '''
    alp = [i for i in string.ascii_lowercase]
    ships = has_ship()
    if lst_cor in ships:
        i = lst_cor[1]
        ship_len = 0
        for ship in ships:
            if i in ship:
                ship_len +=1
        return (ship_len)


def is_valid():
    """
    is_valid
    (data) -> (bool)
    яка перевіряє чи поле зчитане з файлу може бути ігровим полем, на якому
    розмішені усі кораблі
    """
    path = "field.txt"
    lst=read_field(path)
    if len(lst[0])==10 and len(lst)==10:
        return True
    else:
        return False
