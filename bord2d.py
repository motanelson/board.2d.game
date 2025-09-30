print("\033c\033[43;30m\nboard\n")
def build(lena,incx,incy):
    x=0
    y=0
    z=0
    list1=[]
    for n in range(lena):
        l1=[x,y]
        list1=list1+[l1]
        x=x+incx
        y=y+incy
        
    return list1 
def mark(list1,array1,value):
    for n in list1:
        array1[n[1]][n[0]]=value
    return array1
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
    aaa=" "
    for nn in range(x):
        aa=aa+[aaa]
    for n in range(y):
        a=a+[aa]
    return a


a=board2d(16,16)
aaa=build(8,2,2)
a=mark(aaa,a,"X")
draw(a)
