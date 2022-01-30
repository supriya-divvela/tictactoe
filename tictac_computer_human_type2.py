from itertools import combinations, permutations
import random
t=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
def fun(i):
    if i=='3':
        return 'X'
    elif i=='5':
        return 'O'
    else:
        return ' '
def printboard(l):
    print(fun(l[0])+'|'+fun(l[1])+'|'+fun(l[2])+'|'+"\n-+-+-+\n"+fun(l[3])+'|'+fun(l[4])+'|'+fun(l[5])+'|'+"\n-+-+-+\n"+fun(l[6])+'|'+fun(l[7])+'|'+fun(l[8])+'|'+"\n-+-+-+")
m='y'
while(m=='y'):
    l=['2' for i in range(9)]
    printboard(l)
    flag=False
    m=input("Enter Who will play first 3(computer)/5(human):")
    c=0
    while '2' in l:
        if(m=='3'):
            if ((c==1 and m=='3' and l[4]=='2') or (c==0)):l[4]=m
            elif c<3:
                p=random.choice([1,3,7,9])
                if l[p-1]=='2':
                    l[p-1]=m
                else:
                    while l[p-1]!='2':
                        p=random.choice([1,3,7,9])
                        if l[p-1]=='2':
                            l[p-1]=m
                            break
            else:
                t1,t2,t3=[],[],[]
                for i in range(9):
                    if l[i]=='3':t1.append(i)
                    elif l[i]=='5':t2.append(i)
                    else:t3.append(i)
                flag2=False
                for i in list(combinations(t1,2)):
                    for j in t3:
                        if sorted((i[0],i[1],j)) in t:
                            if int(l[i[0]])*int(l[i[1]])*int(l[j])==18:
                                flag2=True
                                l[j]=m
                                break
                if flag2==False:
                    flag3=False
                    for i in list(combinations(t2,2)):
                        for j in t3:
                            if sorted((i[0],i[1],j)) in t:
                                if int(l[i[0]])*int(l[i[1]])*int(l[j])==50:
                                    flag3=True
                                    l[j]=m
                                    break
                    if flag3==False:
                        p=random.choice(t3)
                        l[p-1]=m
            print("Computers board is:")
            printboard(l)    
        else:
            p=int(input(f"Enter in which position u want to place {m}:"))
            if l[p-1]=='2':
                l[p-1]=m
            else:
                while l[p-1]!='2':
                    p=int(input(f"It is already filled...enter another position to place {m}:"))
                    if l[p-1]=='2':
                        l[p-1]=m
                        break
            print("Humans board is:")
            printboard(l)
        s1,s2=[],[]
        for i in range(9):
            if l[i]==m:
                s1.append(i)
        flag=False
        for i in list(combinations(s1,3)):
            if sorted(i) in t:
                flag=True
                print(f"{m} has win the game")
                break
        if flag==True:break
        else:
            if m=='3':m='5'
            else:m="3"
            c+=1
    if flag!=True:print("Its is tie game....!")
    m=input("Do u want to play again(y/n):").lower()
