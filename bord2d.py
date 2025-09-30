print("\033c\033[43;30m\nboard\n")
def draw(arrays):
    print("\033c\033[43;30m\n")
    a="0123456789ABCDEF"
    counts=0
    counts2=0
    print(" "+a)
    for nn in range(len(arrays)):
        print(a[counts2],end="")
        counts=0
        
        for n in range(len(arrays[nn])):
            print(arrays[nn][n],end="")
            counts=counts+1
        print((len(a)-counts)*" "+a[counts2])
        counts2=counts2+1
    print(" "+a)

def board():
    print("\033c\033[43;30m\n")
    a="0123456789ABCDEF"
    print(" "+a)
    for n in a:
        print(n+(" "*16)+n)
    print(" "+a)
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


a=board2d(16,16)
draw(a)
