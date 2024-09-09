def sum_all(a, b):
    try:
        c=False
        for i in range(len(a)):
            if a[i]=='.':
                c=True
        if c:
            a=float(a)
        else:
            a=int(a)
        c = False
        for i in range(len(b)):
            if b[i] == '.':
                c = True
        if c:
            b = float(b)
        else:
            b = int(b)
        return a+b
    except:
        return str(a)+str(b)
print(sum_all(input(), input()))
