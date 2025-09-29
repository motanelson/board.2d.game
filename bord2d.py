print("\033c\033[43;30m\nboard\n")

def board2d(x,y):
    a=[]
    aa=[]
    aaa="X"
    for nn in range(x):
        aa=aa+[aaa]
    for n in range(y):
        a=a+[aa]
    return a


a=board2d(2,2)
print(a)