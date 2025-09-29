print("\033c\033[43;30m\nboard\n")
def saves(files,arrays):
    f1=open(files,"w")
    for n in arrays:
        l=False
        for nn in n:
             if l:
                 f1.write(", "+str(nn))
             else:
                 f1.write(str(nn))
             l=True
        f1.write("\n")
    f1.close()
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
saves("2d.csv",a)
print(a)