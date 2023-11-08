a = input('Введите число A:')
b = input('Введите число B:')
c = input('Введите число C:')
d = input('Введите число D:')
e = input('Введите число E:')
s = input('Введите общее кол-во:')

if a == '?':
    try:
        e = int(e)
        s = int(s)
        a = s - e
    except:
        try:
            b = int(b)
            d = int(d)
            a = d + b
        except:
            print('error! incorrect values!')
    print('Значение А: ', a)
if b == '?':
    try:
        a = int(a)
        d = int(d)
        b = a - d
    except:
        try:
            c = int(c)
            e = int(e)
            b = c - e
        except:
            print('error! incorrect values!')
            try:
                a = int(a)
                c = int(c)
                s = int(s)
                b = a + c - s
            except:
                print('error! incorrect values!')
    print('Значение В: ', b)
if c == '?':
    try:
        b = int(b)
        e = int(e)
        c = b + e
    except:
        try:
            d = int(d)
            s = int(s)
            c = s - d
        except:
            print('error! incorrect values!')
    print('Значение С: ', c)
if d == '?':
    try:
        c = int(c)
        s = int(s)
        d = s - c
    except:
        try:
            a = int(a)
            b = int(b)
            d = a - b
        except:
            print('error! incorrect values!')
    print('Значение D: ', d)
if e == '?':
    try:
        a = int(a)
        s = int(s)
        e = s - a
    except:
        try:
            c = int(c)
            b = int(b)
            e = c - b
        except:
            print('error! incorrect values!')
    print('Значение E: ', e)
if s == '?':
    try:
        a = int(a)
        e = int(e)
        s = a + e
    except:
        try:
            c = int(c)
            d = int(d)
            s = c + d
        except:
            print('error! incorrect values!')
    print('Общее количество: ', s)