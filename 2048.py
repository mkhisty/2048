from tkinter import *
from random import randint
wndw = Tk()
gv = [[StringVar() for i in range (4)]for j in range (4) ]
labels = [[Label(wndw,width=6,height=3,textvariable =gv[i][j],bg='white',relief="sunken",font = ("Helvtica",32)).grid(row=i, column=j)for i in range(0,4)]for j in range(0,4)]
x = randint(0,3)
y =  randint(0,3)
gv[x][y].set("2")
while True:
    x1 = randint(0,3)
    y1 =  randint(0,3)
    if x1!=x and y1!=y:
        gv[x1][y1].set("2")
        break
def rowstocolumns(ng):
    columns=[]
    for v2 in range(0,4):
        column = []
        for v1 in range(0,4):
            column.append(ng[v1][v2])
        columns.append(column)
    return(columns)
def columnstorows(columns):
    ng = [[int()for i in range(4)]for j in range(4)]
    for m in range(4):
        for n in range(4):
            ng[n][m]=columns[m][n]
    return(ng)
def newtile(m,o):
    changed = 0
    for j in range(4):
        for k in range(4):
            if o[k][j]==m[k][j]:
                pass
            else:
                changed = 1
                break
            
    if changed==1:
        zero = False
        for i in range(4):
            t = 0 in m[i]
            if t==True:
                zero = True
        if zero == True:
            while True:
                x = randint(0,3)
                y = randint(0,3)
                if m[x][y]==0:
                    break
            m[x][y] = 2
        return(m)
    return(o)
            
def update(b):
    for i in range(0,4):
        for j in range(0,4):
            x = str(b[i][j])
            if x!="0":
                gv[i][j].set(x)
            else:
                gv[i][j].set("")
def vaccum(c,d):
    if d=="up":
        while True:
            try:
                c.remove(0)
            except:
                break
        for k in range(0,4-len(c)):
            c.append(0)
        return(c)
    else:
        ppd=[]
        c1 = c.copy()
        for x in range(4):

            if c[x]!=0:
                ppd.append(c[x])
                c1.remove(c[x])
        for j in range(len(ppd)):
            c1.append(ppd[j])
        return(c1)
def boardvalues():
    ng = []
    for i in range(4):
        row=[]
        for j in range(4):
            v = gv[i][j]
            if v.get() == "":
                row.append(0)
            else:
                row.append(int(v.get()))
        ng.append(row)
    return(ng)
def move(drc,a):
    ng = boardvalues()

    if a=="x":
        columns = ng
        columns2 = rowstocolumns(ng)
    else:
        columns = rowstocolumns(ng)
        columns2 = columnstorows(ng)
    for i in range(0,4):
        c = columns[i]
        c3 = 0
        c = vaccum(c,drc)
        if drc == "up":
            for l in range(0,4):
                cnt = l
                if cnt!=3:
                
                    if c[cnt]==c[cnt+1] and c3==0:
                        ph = c[cnt+1]
                        c[cnt+1]=0
                        c[cnt] = ph*2
                        mm = c[cnt]
                        c3=1
                    else:
                        c3 = 0
        elif drc =="down":
            for l in range(0,4):
                cnt = 3-l
                if cnt!=0:
                
                    if c[cnt]==c[cnt-1] and c3==0:
                        ph = c[cnt]
                        c[cnt]=0
                        c[cnt-1] = ph*2
                        mm = c[cnt-1]
                        c3=1
                    else:
                        c3 = 0
            
        c = vaccum(c,drc)
        columns[i] = c
    if a!="x":
        ng = columnstorows(columns)
    ng = newtile(ng,columnstorows(columns2))
    update(ng)
wndw.bind("<Up>", lambda a: move("up","y"))
wndw.bind("<Down>", lambda a: move("down","y"))
wndw.bind("<Right>", lambda a: move("down","x"))
wndw.bind("<Left>", lambda a: move("up","x"))
wndw.mainloop()
