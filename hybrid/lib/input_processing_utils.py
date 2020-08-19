def get_skillex(x: str):
    y=[]
    for l in x:
        y.append(l)
    y[len(y)-1] = 'a'
    return ''.join(y)