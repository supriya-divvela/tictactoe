import random
def printboard(l):
    print(l[0]+'|'+l[1]+'|'+l[2]+'|'+"\n-+-+-+\n"+l[3]+'|'+l[4]+'|'+l[5]+'|'+"\n-+-+-+\n"+l[6]+'|'+l[7]+'|'+l[8]+'|'+"\n-+-+-+")
m='y'
while(m=='y'):
    l=[' ' for i in range(9)]
    printboard(l)
    flag=False
    m=input("Enter Who will play first 3(computer)/5(human):")
    c=0
    while ' ' in l:
        if(m=='3'):
            if ((c==1 and m=='3' and l[4]==' ') or (c==0)):l[4]=m
            elif c<3:
                p=random.choice([1,3,7,9])
                if l[p-1]==' ':
                    l[p-1]=m
                else:
                    while l[p-1]!=' ':
                        print(f"It is already filled...enter another position to place {m}:")
                        p=random.choice([1,3,7,9])
                        if l[p-1]==' ':
                            l[p-1]=m
                            break
                print(p)
            else:
                if([l[0],l[1],l[2]]==['3','3',' ']):l[2]='3'
                elif([l[0],l[1],l[2]]==['3',' ','3']):l[1]='3'
                elif([l[0],l[1],l[2]]==[' ','3','3']):l[0]='3'
                elif([l[3],l[4],l[5]]==[' ','3','3']):l[3]='3'
                elif([l[3],l[4],l[5]]==['3',' ','3']):l[4]='3'
                elif([l[3],l[4],l[5]]==['3','3',' ']):l[5]='3'
                elif([l[6],l[7],l[8]]==[' ','3','3']):l[6]='3'
                elif([l[6],l[7],l[8]]==['3',' ','3']):l[7]='3'
                elif([l[6],l[7],l[8]]==['3','3',' ']):l[8]='3'
                elif([l[0],l[3],l[6]]==[' ','3','3']):l[0]='3'
                elif([l[0],l[3],l[6]]==['3',' ','3']):l[3]='3'
                elif([l[0],l[3],l[6]]==['3','3',' ']):l[6]='3'
                elif([l[1],l[4],l[7]]==[' ','3','3']):l[1]='3'
                elif([l[1],l[4],l[7]]==['3',' ','3']):l[4]='3'
                elif([l[1],l[4],l[7]]==['3','3',' ']):l[7]='3'
                elif([l[2],l[5],l[8]]==[' ','3','3']):l[2]='3'
                elif([l[2],l[5],l[8]]==['3',' ','3']):l[5]='3'
                elif([l[2],l[5],l[8]]==['3','3',' ']):l[8]='3'
                elif([l[0],l[4],l[8]]==[' ','3','3']):l[0]='3'
                elif([l[0],l[4],l[8]]==['3',' ','3']):l[4]='3'
                elif([l[0],l[4],l[8]]==['3','3',' ']):l[8]='3'
                elif([l[2],l[4],l[6]]==[' ','3','3']):l[2]='3'
                elif([l[2],l[4],l[6]]==['3',' ','3']):l[4]='3'
                elif([l[2],l[4],l[6]]==['3','3',' ']):l[6]='3'
                elif([l[0],l[1],l[2]]==['5','5',' ']):l[2]='3'
                elif([l[0],l[1],l[2]]==[' ','5','5']):l[0]='3'
                elif([l[0],l[1],l[2]]==['5',' ','5']):l[1]='3'
                elif([l[3],l[4],l[5]]==[' ','5','5']):l[3]='3'
                elif([l[3],l[4],l[5]]==['5',' ','5']):l[4]='3'
                elif([l[3],l[4],l[5]]==['5','5',' ']):l[5]='3'
                elif([l[6],l[7],l[8]]==[' ','5','5']):l[6]='3'
                elif([l[6],l[7],l[8]]==['5',' ','5']):l[7]='3'
                elif([l[6],l[7],l[8]]==['5','5',' ']):l[8]='3'
                elif([l[0],l[3],l[6]]==[' ','5','5']):l[0]='3'
                elif([l[0],l[3],l[6]]==['5',' ','5']):l[3]='3'
                elif([l[0],l[3],l[6]]==['5','5',' ']):l[6]='3'
                elif([l[1],l[4],l[7]]==[' ','5','5']):l[1]='3'
                elif([l[1],l[4],l[7]]==['5',' ','5']):l[4]='3'
                elif([l[1],l[4],l[7]]==['5','5',' ']):l[7]='3'
                elif([l[2],l[5],l[8]]==[' ','5','5']):l[2]='3'
                elif([l[2],l[5],l[8]]==['5',' ','5']):l[5]='3'
                elif([l[2],l[5],l[8]]==['5','5',' ']):l[8]='3'
                elif([l[0],l[4],l[8]]==[' ','5','5']):l[0]='3'
                elif([l[0],l[4],l[8]]==['5',' ','5']):l[4]='3'
                elif([l[0],l[4],l[8]]==['5','5',' ']):l[8]='3'
                elif([l[2],l[4],l[6]]==[' ','5','5']):l[2]='3'
                elif([l[2],l[4],l[6]]==['5',' ','5']):l[4]='3'
                elif([l[2],l[4],l[6]]==['5','5',' ']):l[6]='3'
                else:
                    p=random.choice([i+1 for i in range(len(l)) if l[i]==' '])
                    if l[p-1]==' ':
                        l[p-1]=m
                    else:
                        while l[p-1]!=' ':
                            print(f"It is already filled...enter another position to place {m}:")
                            p=random.choice([i+1 for i in range(len(l)) if l[i]==' '])
                            if l[p-1]==' ':
                                l[p-1]=m
                                break 
            print("Computers board is:")
            printboard(l)    
        else:
            p=int(input(f"Enter in which position u want to place {m}:"))
            if l[p-1]==' ':
                l[p-1]=m
            else:
                while l[p-1]!=' ':
                    p=int(input(f"It is already filled...enter another position to place {m}:"))
                    if l[p-1]==' ':
                        l[p-1]=m
                        break
            print("Humans board is:")
            printboard(l)
        if((l[0]==l[1]==l[2]=="3" or l[0]==l[1]==l[2]=="5")or(l[3]==l[4]==l[5]=="3" or l[3]==l[4]==l[5]=="5") or (l[6]==l[7]==l[8]=="3" or l[6]==l[7]==l[8]=="5") or (l[0]==l[3]==l[6]=="3" or l[0]==l[3]==l[6]=="5") or (l[1]==l[4]==l[7]=="3" or l[1]==l[4]==l[7]=="5") or (l[2]==l[5]==l[8]=="3" or l[2]==l[5]==l[8]=="5") or (l[0]==l[4]==l[8]=="3" or l[0]==l[4]==l[8]=="5") or (l[2]==l[4]==l[6]=="3" or l[2]==l[4]==l[6]=="5")):
            printboard(l)
            flag=True
            print(f"{m} has win the game")
            break
        if m=='3':m='5'
        else:m="3"
        c+=1
    if flag!=True:
        print("Its is tie game....!")
    m=input("Do u want to play again(y/n):").lower()
