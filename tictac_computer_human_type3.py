from itertools import combinations
import random
def printboard(l):
    print(l[0]+'|'+l[1]+'|'+l[2]+'|'+"\n-+-+-+\n"+l[3]+'|'+l[4]+'|'+l[5]+'|'+"\n-+-+-+\n"+l[6]+'|'+l[7]+'|'+l[8]+'|'+"\n-+-+-+")
m='y'
q=[8,1,6,3,5,7,4,9,2]
while(m=='y'):
    l=[' ' for i in range(9)]
    printboard(l)
    flag=False
    m=input("Enter Who will play first X(computer)/O(human):")
    c=0
    while ' ' in l:
        if(m=='X'):
            if ((c==1 and m=='X' and l[4]==' ') or (c==0)):l[4]=m
            elif c<3:
                p=random.choice([1,3,7,9])
                if l[p-1]==' ':l[p-1]=m
                else:
                    while l[p-1]!=' ':
                        p=random.choice([1,3,7,9])
                        if l[p-1]==' ':
                            l[p-1]=m
                            break
            else:
                t1,t2,t3=[],[],[]
                for i in range(9):
                    if l[i]=='X':t1.append(q[i])
                    elif l[i]=='O':t2.append(q[i])
                    else:t3.append(q[i])
                flag2=False
                for i in list(combinations(t1,2)):
                    if (15-sum(i) in q) and (l[q.index(15-sum(i))]==' '):
                        flag2=True
                        l[q.index(15-sum(i))]=m
                        break
                if flag2==False:
                    flag3=False
                    for i in list(combinations(t2,2)):
                        if (15-sum(i) in q) and (l[q.index(15-sum(i))]==' '):
                            flag3=True
                            l[q.index(15-sum(i))]=m
                            break
                    if flag3==False:
                        p=random.choice(t3)
                        l[p-1]=m
            print("Computers board is:")
            printboard(l)    
        else:
            p=int(input(f"Enter in which position u want to place {m}:"))
            if l[p-1]==' ':l[p-1]=m
            else:
                while l[p-1]!=' ':
                    p=int(input(f"It is already filled...enter another position to place {m}:"))
                    if l[p-1]==' ':
                        l[p-1]=m
                        break
            print("Humans board is:")
            printboard(l)
        s1=[]
        flag=False
        for i in range(9):
            if l[i]==m:
                s1.append(q[i])
        for i in list(combinations(s1,3)):
            if sum(i)==15:
                flag=True
                print(f"{m} has win the game")
        if flag==True:break
        else:
            if m=='X':m='O'
            else:m="X"
            c+=1
    if flag!=True:print("Its is tie game....!")
    m=input("Do u want to play again(y/n):").lower()
'''
output:
 | | |
-+-+-+
 | | |
-+-+-+
 | | |
-+-+-+
Enter Who will play first X(computer)/O(human):O
Enter in which position u want to place O:3
Humans board is:
 | |O|
-+-+-+
 | | |
-+-+-+
 | | |
-+-+-+
Computers board is:
 | |O|
-+-+-+
 |X| |
-+-+-+
 | | |
-+-+-+
Enter in which position u want to place O:2
Humans board is:
 |O|O|
-+-+-+
 |X| |
-+-+-+
 | | |
-+-+-+
Computers board is:
X|O|O|
-+-+-+
 |X| |
-+-+-+
 | | |
-+-+-+
Enter in which position u want to place O:4
Humans board is:
X|O|O|
-+-+-+
O|X| |
-+-+-+
 | | |
-+-+-+
Computers board is:
X|O|O|
-+-+-+
O|X| |
-+-+-+
 | |X|
-+-+-+
X has win the game
Do u want to play again(y/n):n
'''
