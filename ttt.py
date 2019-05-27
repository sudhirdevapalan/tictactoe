import sys
import random
import os
x=[]
xx=[]
yy=[]
global smart,log,count
def disp():
    global x
    print "\n",x[0],"| "+x[1],"| "+x[2]
    print "---------"
    print x[3],"|",x[4],"|",x[5]
    print "---------"
    print x[6],"|",x[7]+" |",x[8],"\n"

def check():
    global x
    if x[3]==x[4]==x[5]  or x[1]==x[4]==x[7]  or x[0]==x[4]==x[8] or x[2]==x[4]==x[6]:
        if x[4]=='X':
            print "Player-1 wins"
        else:
            print "Player-2 wins"
        sys.exit(0)
    if x[0]==x[1]==x[2] or x[0]==x[3]==x[6]:
        if x[0]=='X':
            print "Player-1 wins"
        else:
            print "Player-2 wins"
        sys.exit(0)
    if x[6]==x[7]==x[8] or x[2]==x[5]==x[8]:
        if x[8]=='X':
            print "Player-1 wins"
        else:
            print "Player-2 wins"
        sys.exit(0)
    i=0
    while i<=9:
        if x[i]!='X' and x[i]!='Y':
            break
        i=i+1
        if i==9:
            print "Game drawn!"
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
    global x,xx,yy,smart,log,count
    log=9
    count=0
    for i in range(9):
        if x[i]=='X':
            xx[i]='1'
        if x[i]=='Y':
            yy[i]='1'
    while 1:
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
    elif (int(yy[0])+int(yy[1])+int(yy[2]))==2 and (int(xx[0])+int(xx[1])+int(xx[2]))==0:
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
    elif (int(yy[0])+int(yy[1])+int(yy[2]))==0 and (int(xx[0])+int(xx[1])+int(xx[2]))==2:
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
    elif count==1:
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
    elif ((int(xx[0])+int(xx[1])+int(xx[2])+int(xx[3])+int(xx[4])+int(xx[5])+int(xx[6])+int(xx[7])+int(xx[8]))==1):
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

    else:
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
    disp()
    check()


'''    elif (int(xx[1])+int(xx[3])==2):
        x[int(random.sample([0,2,6],1)[0])]="Y"
    elif (int(xx[1])+int(xx[5])==2):
        x[int(random.sample([0,2,8],1)[0])]="Y"
    elif (int(xx[5])+int(xx[7])==2):
        x[int(random.sample([2,6,8],1)[0])]="Y"
    elif (int(xx[3])+int(xx[7])==2):
        x[int(random.sample([0,6,8],1)[0])]="Y"
'''
def comp1():
    global x,xx,yy
    for i in range(9):
        if x[i]=='X':
	    xx[i]='1'
        if x[i]=='Y':
	    yy[i]='1'
    if (int(yy[0])+int(yy[1])+int(yy[2]))==2 and (int(xx[0])+int(xx[1])+int(xx[2]))==0:
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
    elif (int(yy[0])+int(yy[1])+int(yy[2]))==0 and (int(xx[0])+int(xx[1])+int(xx[2]))==2:
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
    elif (int(yy[0])+int(yy[2])+int(yy[4])+int(yy[6])+int(yy[8])+int(xx[0])+int(xx[2])+int(xx[4])+int(xx[6])+int(xx[8]))<5:
        s=[]
        if x[4]=="4":
            s.append("4")
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
    else:
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
    disp()
    check()



def comp2():
    global x,xx,yy
    for i in range(9):
        if x[i]=='X':
            xx[i]='1'
        if x[i]=='Y':
            yy[i]='1'
    if (int(yy[0])+int(yy[1])+int(yy[2]))==2 and (int(xx[0])+int(xx[1])+int(xx[2]))==0:
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
    elif (int(yy[0])+int(yy[1])+int(yy[2]))==0 and (int(xx[0])+int(xx[1])+int(xx[2]))==2:
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
    else:
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
    disp()
    check()




def player1():
    print "Player-1:"
    global smart
    smart=-1
    flag=0
    while flag!=1:
        p1=raw_input("Select an option:")
        try:
            if int(p1)>=0 and int(p1)<9 and x[int(p1)]==str(p1):
                flag=1
            else:
                print "Invalid option!"
        except:
            print "Enter a valid number!"
    i=0
    while i<9:
        if x[i]==str(p1):
            x[i]="X"
        i=i+1
    disp()
    check()

def player2():
    disp()
    print "Player-2:"
    flag=0
    while flag!=1:
        p2=raw_input("Select an option:")
        try:
            if int(p2)>=0 and int(p2)<9 and x[int(p2)]==str(p2):
                flag=1
            else:
                print "Invalid option!"
        except:
            print "Enter a valid number!"
    i=0
    while i<9:
        if x[i]==str(p2):
            x[i]="Y"
        i=i+1
    disp()
    check()






i=0
while i<9:
    x.append(str(i))
    i=i+1

for i in range(9):
    xx.append("0")
    yy.append("0")

print "TIC TAC TOE\n"
opt=2
while(opt!="2" or opt!="c"):
    opt=raw_input("To play with computer type c and to play versus human type 2: ")
    if opt=="2":
        disp()
        while 1:
            player1()
            player2()
    elif opt=="c":
        print "Select difficulty:\nEasy-1\nMedium-2\nHard-3\n"
        opt1="y"
        #diff="1"
        while 1:
            diff=raw_input("Enter your option:")
            if diff!="1" and diff!="2" and diff!="3":
                print "Enter valid value!"
                continue
            else:
                #print "hello"
                break
        if diff=="3":
            while(opt1!="y" or opt1!="n"):
                opt1=raw_input("Do you want to begin the game??(y/n): ")
                if opt1=="y":
                    disp()
                    while 1:
                        player1()
                        comp()
                elif opt1=="n":
                    disp()
                    while 1:
                        comp()
                        player1()
                else:
                    print "Invalid option"
        elif diff=="2":
            while(opt1!="y" or opt1!="n"):
                opt1=raw_input("Do you want to begin the game??(y/n): ")
                if opt1=="y":
                    disp()
                    while 1:
                        player1()
                        comp1()
                elif opt1=="n":
                    disp()
                    while 1:
                        comp1()
                        player1()
                else:
                    print "Invalid option"
            #os.system("python ttt1.py")
            #sys.exit(0)
        else:
            while(opt1!="y" or opt1!="n"):
                opt1=raw_input("Do you want to begin the game??(y/n): ")
                if opt1=="y":
                    disp()
                    while 1:
                        player1()
                        comp2()
                elif opt1=="n":
                    disp()
                    while 1:
                        comp2()
                        player1()
                else:
                    print "Invalid option"
            #os.system("python ttt2.py")
            #sys.exit(0)
    else:
        print "Invalid option"


'''
while 1:
    print "Player-1:"
    flag=0
    while flag!=1:
        p1=raw_input("Select an option:")
        try:
            if int(p1)>=0 and int(p1)<9 and x[int(p1)]==str(p1):
                flag=1
            else:
                print "Invalid option!"
        except:
            print "Enter a valid number!"
    i=0
    while i<9:
        if x[i]==str(p1):
            x[i]="X"
        i=i+1
    disp()
    check()
    comp()
    disp()
    check()

    print "Player-2:"
    flag=0
    while flag!=1:
        p2=raw_input("Select an option:")
        try:
            if int(p2)>=0 and int(p2)<9 and x[int(p2)]==str(p2):
                flag=1
            else:
                print "Invalid option!"
        except:
            print "Enter a valid number!"
    i=0
    while i<9:
        if x[i]==str(p2):
            x[i]="Y"
        i=i+1
    disp()
    check()
'''

'''
        if log==0 and (int(xx[4])+int(xx[8]))<2:
            x[0]='Y'
        elif log==1:
            x[1]='Y'
        elif log==2 and (int(xx[4])+int(xx[6]))<2:
            x[2]='Y'
        elif log==3:
            x[3]='Y'
        elif log==4 and ((int(xx[0])+int(xx[8]))<2) and ((int(xx[2])+int(xx[6]))<2):
            x[4]='Y'
        elif log==5:
            x[5]='Y'
        elif log==6 and (int(xx[2])+int(xx[4]))<2:
            x[6]='Y'
        elif log==7:
            x[7]='Y'
        elif log==8 and (int(xx[0])+int(xx[4]))<2:
            x[8]='Y'
'''

