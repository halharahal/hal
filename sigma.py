def formula(k):
    return k * k

def sigma(formula, frm, to):
    result = 0
    for i in range(frm, to+1):
        result += formula(i)
    print(result)ß

sigma(formula, 1, 6)
