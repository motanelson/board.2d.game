print("\033c\033[43;30m\nboard\n")
#print("\033c\033[43;30m\nboard\n")
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
        
        xx=n[0]
        yy=n[1]
        
        array1[yy][xx]=value
           
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
            i=arrays[nn][n]
            #print(i)
            print(i,end="")
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
    a=" "
    b=[]
    c=[]
    for xx in range(x):
        b=b+[a]
    for yy in range(y):
        c=c+[b.copy()]
    
    return c



a=board2d(15,15)
aaa=build(8,2,2)
#print(a)
a=mark(aaa,a,"X")
#print(a)
draw(a)
