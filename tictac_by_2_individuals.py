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
        if l[p-1]==' ':
            l[p-1]=m
        else:
            while l[p-1]!=' ':
                    p=int(input(f"It is already filled...enter another position to place {m}:"))
                    if l[p-1]==' ':
                        l[p-1]=m
                        break
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
    
'''
output:
 | | |
-+-+-+
 | | |
-+-+-+
 | | |
-+-+-+
Enter Who will play first:(X/O):X
Enter in which position u want to place X:5
 | | |
-+-+-+
 |X| |
-+-+-+
 | | |
-+-+-+
Enter in which position u want to place O:1
O| | |
-+-+-+
 |X| |
-+-+-+
 | | |
-+-+-+
Enter in which position u want to place X:9
O| | |
-+-+-+
 |X| |
-+-+-+
 | |X|
-+-+-+
Enter in which position u want to place O:7
O| | |
-+-+-+
 |X| |
-+-+-+
O| |X|
-+-+-+
Enter in which position u want to place X:3
O| |X|
-+-+-+
 |X| |
-+-+-+
O| |X|
-+-+-+
Enter in which position u want to place O:4
O| |X|
-+-+-+
O|X| |
-+-+-+
O| |X|
-+-+-+
O has win the game
Do u want to play again(y/n):n
'''
