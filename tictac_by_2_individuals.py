def printboard(l):
    print(l[0]+'|'+l[1]+'|'+l[2]+'|'+"\n-+-+-+\n"+l[3]+'|'+l[4]+'|'+l[5]+'|'+"\n-+-+-+\n"+l[6]+'|'+l[7]+'|'+l[8]+'|'+"\n-+-+-+")
m='y'
while(m=='y'):
    l=[' ' for i in range(9)]
    printboard(l)
    flag=False
    m=input("Enter Who will play first:(X/O):")
    while ' ' in l:
        p=int(input(f"Enter in which position u want to place {m}:"))
        if l[p-1]==' ':l[p-1]=m
        else:print("It is already filled...enter another position..!")
        if((l[0]==l[1]==l[2]=="X" or l[0]==l[1]==l[2]=="O")or(l[3]==l[4]==l[5]=="X" or l[3]==l[4]==l[5]=="O") or (l[6]==l[7]==l[8]=="X" or l[6]==l[7]==l[8]=="O") or (l[0]==l[3]==l[6]=="X" or l[0]==l[3]==l[6]=="O") or (l[1]==l[4]==l[7]=="X" or l[1]==l[4]==l[7]=="O") or (l[2]==l[5]==l[8]=="X" or l[2]==l[5]==l[8]=="O") or (l[0]==l[4]==l[8]=="X" or l[0]==l[4]==l[8]=="O") or (l[2]==l[4]==l[6]=="X" or l[2]==l[4]==l[6]=="O")):
            printboard(l)
            flag=True
            print(f"{m} has win the game")
            break
        printboard(l)
        if m=='X':m='O'
        else:m="X"
    if flag!=True:
        print("Its is tie game....!")
    m=input("Do u want to play again(y/n):").lower()
