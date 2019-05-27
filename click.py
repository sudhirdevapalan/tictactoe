import Tkinter
from Tkinter import *
import tkMessageBox
import random
import sys
import os
global log,x,xx,yy,smart,count,p,can,c,b0,b1,b2,b3,b4,b5,b6,b7,b8
c=Tkinter.Tk()
can=Tkinter.Canvas(c,bg="black",height="1000",width="1000")

l=Label(c,text="TIC TAC TOE",font=("Times New Roman",20),bg="black",fg="red")
l.pack(side=TOP,fill="both")

p=0
x=[]
xx=[]
yy=[]
i=0

while i<9:
    x.append(str(i))
    i=i+1

for i in range(9):
    xx.append("0")
    yy.append("0")


def master0():
    global x
    b0.configure(state=DISABLED, text="X",disabledforeground="red")
    x[0]='X'
    check()
    comp()

def master1():
    global x
    b1.configure(state=DISABLED, text="X",disabledforeground="red")
    x[1]='X'
    check()
    comp()

def master2():
    global x
    b2.configure(state=DISABLED, text="X",disabledforeground="red")
    x[2]='X'
    check()
    comp()

def master3():
    global x
    b3.configure(state=DISABLED, text="X",disabledforeground="red")
    x[3]='X'
    check()
    comp()

def master4():
    global x
    b4.configure(state=DISABLED, text="X",disabledforeground="red")
    x[4]='X'
    check()
    comp()

def master5():
    global x
    b5.configure(state=DISABLED, text="X",disabledforeground="red")
    x[5]='X'
    check()
    comp()

def master6():
    global x
    b6.configure(state=DISABLED, text="X",disabledforeground="red")
    x[6]='X'
    check()
    comp()

def master7():
    global x
    b7.configure(state=DISABLED, text="X",disabledforeground="red")
    x[7]='X'
    check()
    comp()

def master8():
    global x
    b8.configure(state=DISABLED, text="X",disabledforeground="red")
    x[8]='X'
    check()
    comp()





def check():
    global x
    if x[3]==x[4]==x[5]  or x[1]==x[4]==x[7]  or x[0]==x[4]==x[8] or x[2]==x[4]==x[6]:
        if x[4]=='X':
            tkMessageBox.showinfo("Victory","Player-1 wins")
        else:
            tkMessageBox.showinfo("Lost","Computer wins")
        sys.exit(0)
    if x[0]==x[1]==x[2] or x[0]==x[3]==x[6]:
        if x[0]=='X':
            tkMessageBox.showinfo("Victory","Player-1 wins")
        else:
            tkMessageBox.showinfo("Lost","Computer wins")
        sys.exit(0)
    if x[6]==x[7]==x[8] or x[2]==x[5]==x[8]:
        if x[8]=='X':
            tkMessageBox.showinfo("Victory","Player-1 wins")
        else:
            tkMessageBox.showinfo("Lost","Computer wins")
        sys.exit(0)
    i=0
    while i<=9:
        if x[i]!='X' and x[i]!='Y':
            break
        i=i+1
        if i==9:
            tkMessageBox.showinfo("No more moves","Game drawn!!")
            sys.exit(0)

def minval(a,b,c):
    global xx
    if xx[a]=='0':
        return a
    elif xx[b]=='0':
        return b
    else:
        return c

def comp():
    global x,xx,yy,smart,log,count,b0,b1,b2,b3,b4,b5,b6,b7,b8
    chk=[]
    chk1=[]
    log=9
    count=0
    smart=-1
    for i in range(9):
        if x[i]=='X':
            xx[i]='1'
	    chk.append(i)
        if x[i]=='Y':
            yy[i]='1'
	    chk.append(i)
    while 1:						#Next decision
	if x[0]=='0':
	    xx[0]='1'
	    if (((int(xx[0])+int(xx[1])+int(xx[2]))==2 and ((int(yy[1])+int(yy[2]))==0)) and ((int(xx[0])+int(xx[3])+int(xx[6]))==2 and ((int(yy[3])+int(yy[6]))==0))) or (((int(xx[0])+int(xx[4])+int(xx[8]))==2 and ((int(yy[4])+int(yy[8]))==0)) and ((int(xx[0])+int(xx[1])+int(xx[2]))==2 and ((int(yy[1])+int(yy[2]))==0))) or (((int(xx[0])+int(xx[4])+int(xx[8]))==2 and ((int(yy[4])+int(yy[8]))==0)) and ((int(xx[0])+int(xx[3])+int(xx[6]))==2 and ((int(yy[3])+int(yy[6]))==0))):
		xx[0]='0'
		log=0
		count=count+1
		#break
	    else:
	        #log=9
		xx[0]='0'
	if x[1]=='1':
	    xx[1]='1'
            if ((int(xx[0])+int(xx[1])+int(xx[2]))==2 and ((int(yy[1])+int(yy[2]))==0)) and ((int(xx[1])+int(xx[4])+int(xx[7]))==2 and ((int(yy[4])+int(yy[7]))==0)):
		xx[1]='0'
		log=1
		count=count+1
		#break
	    else:
	        #log=9
		xx[1]='0'
	if x[2]=='2':
	    xx[2]='1'
	    if (((int(xx[0])+int(xx[1])+int(xx[2]))==2 and ((int(yy[0])+int(yy[1]))==0)) and ((int(xx[2])+int(xx[5])+int(xx[8]))==2 and ((int(yy[5])+int(yy[8]))==0))) or (((int(xx[2])+int(xx[4])+int(xx[6]))==2 and ((int(yy[4])+int(yy[6]))==0)) and ((int(xx[0])+int(xx[1])+int(xx[2]))==2 and ((int(yy[0])+int(yy[1]))==0))) or (((int(xx[2])+int(xx[4])+int(xx[6]))==2 and ((int(yy[4])+int(yy[6]))==0)) and ((int(xx[2])+int(xx[5])+int(xx[8]))==2 and ((int(yy[5])+int(yy[8]))==0))):
		xx[2]='0'
		log=2
		count=count+1
		#break
	    else:
	        #log=9
		xx[2]='0'
	if x[3]=='3':
	    xx[3]='1'
            if ((int(xx[0])+int(xx[3])+int(xx[6]))==2 and ((int(yy[0])+int(yy[6]))==0)) and ((int(xx[3])+int(xx[4])+int(xx[5]))==2 and ((int(yy[4])+int(yy[5]))==0)):
		xx[3]='0'
		log=3
		count=count+1
		#break
	    else:
	        #log=9
		xx[3]='0'
	if x[5]=='5':
	    xx[5]='1'
            if ((int(xx[3])+int(xx[4])+int(xx[5]))==2 and ((int(yy[3])+int(yy[4]))==0)) and ((int(xx[2])+int(xx[5])+int(xx[8]))==2 and ((int(yy[2])+int(yy[8]))==0)):
		xx[5]='0'
		log=5
		count=count+1
		#break
	    else:
	        #log=9
		xx[5]='0'
	if x[6]=='6':
	    xx[6]='1'
	    if (((int(xx[6])+int(xx[7])+int(xx[8]))==2 and ((int(yy[7])+int(yy[8]))==0)) and ((int(xx[0])+int(xx[3])+int(xx[6]))==2 and ((int(yy[0])+int(yy[3]))==0))) or (((int(xx[6])+int(xx[4])+int(xx[2]))==2 and ((int(yy[2])+int(yy[4]))==0)) and ((int(xx[6])+int(xx[7])+int(xx[8]))==2 and ((int(yy[7])+int(yy[8]))==0))) or (((int(xx[6])+int(xx[4])+int(xx[2]))==2 and ((int(yy[2])+int(yy[4]))==0)) and ((int(xx[0])+int(xx[3])+int(xx[6]))==2 and ((int(yy[0])+int(yy[3]))==0))):
		xx[6]='0'
		log=6
		count=count+1
		#break
	    else:
	        #log=9
		xx[6]='0'
	if x[7]=='7':
	    xx[7]='1'
            if ((int(xx[6])+int(xx[7])+int(xx[8]))==2 and ((int(yy[6])+int(yy[8]))==0)) and ((int(xx[1])+int(xx[4])+int(xx[7]))==2 and ((int(yy[1])+int(yy[4]))==0)):
		xx[7]='0'
		log=7
		count=count+1
		#break
	    else:
	        #log=9
		xx[7]='0'
	if x[8]=='8':
	    xx[8]='1'
            if (((int(xx[6])+int(xx[7])+int(xx[8]))==2 and ((int(yy[6])+int(yy[7]))==0)) and ((int(xx[2])+int(xx[5])+int(xx[8]))==2 and ((int(yy[2])+int(yy[5]))==0))) or (((int(xx[0])+int(xx[4])+int(xx[8]))==2 and ((int(yy[0])+int(yy[4]))==0)) and ((int(xx[6])+int(xx[7])+int(xx[8]))==2 and ((int(yy[6])+int(yy[7]))==0))) or (((int(xx[0])+int(xx[4])+int(xx[8]))==2 and ((int(yy[0])+int(yy[4]))==0)) and ((int(xx[2])+int(xx[5])+int(xx[8]))==2 and ((int(yy[2])+int(yy[5]))==0))):
		xx[8]='0'
		log=8
		count=count+1
		break
	    else:
		xx[8]='0'
		#log=9
		break
	else:
	    break
    print "log", log
    if x[4]=="X":
        smart=1
    if x[4]=="4":
        #smart=1
        x[4]="Y"
    elif (int(yy[0])+int(yy[1])+int(yy[2]))==2 and (int(xx[0])+int(xx[1])+int(xx[2]))==0:		#Winning move
        x[0]="Y"
        x[1]="Y"
        x[2]="Y"
    elif (int(yy[0])+int(yy[3])+int(yy[6]))==2 and (int(xx[0])+int(xx[3])+int(xx[6]))==0:
        x[0]="Y"
        x[3]="Y"
        x[6]="Y"
    elif (int(yy[1])+int(yy[4])+int(yy[7]))==2 and (int(xx[1])+int(xx[4])+int(xx[7]))==0:
        x[1]="Y"
        x[4]="Y"
        x[7]="Y"
    elif (int(yy[2])+int(yy[5])+int(yy[8]))==2 and (int(xx[2])+int(xx[5])+int(xx[8]))==0:
        x[2]="Y"
        x[5]="Y"
        x[8]="Y"
    elif (int(yy[3])+int(yy[4])+int(yy[5]))==2 and (int(xx[3])+int(xx[4])+int(xx[5]))==0:
        x[3]="Y"
        x[4]="Y"
        x[5]="Y"
    elif (int(yy[6])+int(yy[7])+int(yy[8]))==2 and (int(xx[6])+int(xx[7])+int(xx[8]))==0:
        x[6]="Y"
        x[7]="Y"
        x[8]="Y"
    elif (int(yy[0])+int(yy[4])+int(yy[8]))==2 and (int(xx[0])+int(xx[4])+int(xx[8]))==0:
        x[0]="Y"
        x[4]="Y"
        x[8]="Y"
    elif (int(yy[2])+int(yy[4])+int(yy[6]))==2 and (int(xx[2])+int(xx[4])+int(xx[6]))==0:
        x[2]="Y"
        x[4]="Y"
        x[6]="Y"
    elif (int(yy[0])+int(yy[1])+int(yy[2]))==0 and (int(xx[0])+int(xx[1])+int(xx[2]))==2:		#Preventing loss
        x[int(minval(0,1,2))]="Y"
    elif (int(yy[0])+int(yy[3])+int(yy[6]))==0 and (int(xx[0])+int(xx[3])+int(xx[6]))==2:
        x[int(minval(0,3,6))]="Y"
    elif (int(yy[1])+int(yy[4])+int(yy[7]))==0 and (int(xx[1])+int(xx[4])+int(xx[7]))==2:
        x[int(minval(1,4,7))]="Y"
    elif (int(yy[2])+int(yy[5])+int(yy[8]))==0 and (int(xx[2])+int(xx[5])+int(xx[8]))==2:
        x[int(minval(2,5,8))]="Y"
    elif (int(yy[3])+int(yy[4])+int(yy[5]))==0 and (int(xx[3])+int(xx[4])+int(xx[5]))==2:
        x[int(minval(3,4,5))]="Y"
    elif (int(yy[6])+int(yy[7])+int(yy[8]))==0 and (int(xx[6])+int(xx[7])+int(xx[8]))==2:
        x[int(minval(6,7,8))]="Y"
    elif (int(yy[0])+int(yy[4])+int(yy[8]))==0 and (int(xx[0])+int(xx[4])+int(xx[8]))==2:
        x[int(minval(0,4,8))]="Y"
    elif (int(yy[2])+int(yy[4])+int(yy[6]))==0 and (int(xx[2])+int(xx[4])+int(xx[6]))==2:
        x[int(minval(2,4,6))]="Y"
    elif count==1:											#Decision
        if log==0:
            x[0]='Y'
        elif log==1:
            x[1]='Y'
        elif log==2:
            x[2]='Y'
        elif log==3:
            x[3]='Y'
        elif log==4:
            x[4]='Y'
        elif log==5:
            x[5]='Y'
        elif log==6:
            x[6]='Y'
        elif log==7:
            x[7]='Y'
        elif log==8:
            x[8]='Y'
    elif ((int(xx[0])+int(xx[1])+int(xx[2])+int(xx[3])+int(xx[4])+int(xx[5])+int(xx[6])+int(xx[7])+int(xx[8]))==1):	#Smart decisions
        s=[]
        if x[0]=="0":
            s.append("0")
        if x[2]=="2":
            s.append("2")
        if x[6]=="6":
            s.append("6")
        if x[8]=="8":
            s.append("8")
        x[int(random.sample(s,1)[0])]="Y"
        del s[:]
    elif (int(yy[1])+int(yy[3])+int(yy[5])+int(yy[7])+int(xx[1])+int(xx[3])+int(xx[5])+int(xx[7]))<4 and smart!=1: 
        s=[]
        print "smart is 0"
        if x[1]=="1":
            s.append("1")
        if x[3]=="3":
            s.append("3")
        if x[5]=="5":
            s.append("5")
        if x[7]=="7":
            s.append("7")
        x[int(random.sample(s,1)[0])]="Y"
        del s[:]
    elif (int(yy[0])+int(yy[2])+int(yy[4])+int(yy[6])+int(yy[8])+int(xx[0])+int(xx[2])+int(xx[4])+int(xx[6])+int(xx[8]))<5 and smart==1:
        s=[]
        print "smart is 1"
        if x[0]=="0":
            s.append("0")
        if x[2]=="2":
            s.append("2")
        if x[6]=="6":
            s.append("6")
        if x[8]=="8":
            s.append("8")
        x[int(random.sample(s,1)[0])]="Y"
        del s[:]

    else:										#Else random
        p=[]
        if x[1]=="1":
            p.append("1")
        if x[3]=="3":
            p.append("3")
        if x[5]=="5":
            p.append("5")
        if x[7]=="7":
            p.append("7")
        if x[0]=="0":
            p.append("0")
        if x[2]=="2":
            p.append("2")
        if x[4]=="4":
            p.append("4")
        if x[6]=="6":
            p.append("6")
        if x[8]=="8":
            p.append("8")
        x[int(random.sample(p,1)[0])]="Y"
        del p[:]
    for i in range(9):
        if x[i]=='X':
	    chk1.append(i)
        if x[i]=='Y':
	    chk1.append(i)
    b=-1
    print chk
    print chk1
    for a in chk1:
        if a not in chk:
	    b=a
	    break
    print b
    if b==0:
        b0.configure(state=DISABLED, text="Y",disabledforeground="yellow")
    elif b==1:
        b1.configure(state=DISABLED, text="Y",disabledforeground="yellow")
    elif b==2:
        b2.configure(state=DISABLED, text="Y",disabledforeground="yellow")
    elif b==3:
        b3.configure(state=DISABLED, text="Y",disabledforeground="yellow")
    elif b==4:
        #print "hello"
        b4.configure(state=DISABLED, text="Y",disabledforeground="yellow")
    elif b==5:
        b5.configure(state=DISABLED, text="Y",disabledforeground="yellow")
    elif b==6:
        b6.configure(state=DISABLED, text="Y",disabledforeground="yellow")
    elif b==7:
        b7.configure(state=DISABLED, text="Y",disabledforeground="yellow")
    elif b==8:
        b8.configure(state=DISABLED, text="Y",disabledforeground="yellow")
    print "$$$$$$$$$$$$$$$"
    check()



b0=Button(can,text="0",command=master0,fg="green",bg="black",font=("Times New Roman",24),activebackground="black",activeforeground="red", width=7,height=4)
b0.grid(row=0, column=0)
b1=Button(can,text="1",command=master1,fg="green",bg="black",font=("Times New Roman",24),activebackground="black",activeforeground="red", width=7,height=4)
b1.grid(row=0,column=1)
b2=Button(can,text="2",command=master2,fg="green",bg="black",font=("Times New Roman",24),activebackground="black",activeforeground="red", width=7,height=4)
b2.grid(row=0, column=2)
b3=Button(can,text="3",command=master3,fg="green",bg="black",font=("Times New Roman",24),activebackground="black",activeforeground="red", width=7,height=4)
b3.grid(row=1, column=0)
b4=Button(can,text="4",command=master4,fg="green",bg="black",font=("Times New Roman",24),activebackground="black",activeforeground="red", width=7,height=4)
b4.grid(row=1, column=1)
b5=Button(can,text="5",command=master5,fg="green",bg="black",font=("Times New Roman",24),activebackground="black",activeforeground="red", width=7,height=4)
b5.grid(row=1, column=2)
b6=Button(can,text="6",command=master6,fg="green",bg="black",font=("Times New Roman",24),activebackground="black",activeforeground="red", width=7,height=4)
b6.grid(row=2, column=0)
b7=Button(can,text="7",command=master7,fg="green",bg="black",font=("Times New Roman",24),activebackground="black",activeforeground="red", width=7,height=4)
b7.grid(row=2, column=1)
b8=Button(can,text="8",command=master8,fg="green",bg="black",font=("Times New Roman",24),activebackground="black",activeforeground="red", width=7,height=4)
b8.grid(row=2, column=2)
can.pack()


c.mainloop()