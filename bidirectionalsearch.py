d={
    '0':['4'],
    '1':['4'],
    '2':['5'],
    '3':['5'],
    '4':['0','1','6'],
    '5':['2','3','6'],
    '6':['4','5','7'],
    '7':['6','8'],
    '8':['7','9','10'],
    '9':['8','11','12'],
    '10':['8','13','14'],
    '11':['9'],
    '12':['9'],
    '13':['10'],
    '14':['10']
}
s='0'
g='15'
if g in d.keys():
    flag=False
    ol1,cl1,ol2,cl2=[s],[s],[g],[g]
    while len(ol1) and len(ol2):
        print("From start",ol1,cl1)
        print("From Goal",ol2,cl2)
        if len(list(set(ol1).intersection(set(ol2))))>0:
            flag=True
            print("Path Exists Between start and goal node.")
            break
        p,q=ol1.pop(0),ol2.pop(0)
        for i in d[p]:
            if i not in cl1:
                ol1.append(i)
                cl1.append(i)
        for i in d[q]:
            if i not in cl2:
                ol2.append(i)
                cl2.append(i)
    if flag==False:
        print("No Path Exists.")
else:
    print("No such node exits.")
    
    
'''
output:
From start ['0'] ['0']
From Goal ['12'] ['12']
From start ['4'] ['0', '4']
From Goal ['9'] ['12', '9']
From start ['1', '6'] ['0', '4', '1', '6']
From Goal ['8', '11'] ['12', '9', '8', '11']
From start ['6'] ['0', '4', '1', '6']
From Goal ['11', '7', '10'] ['12', '9', '8', '11', '7', '10']
From start ['5', '7'] ['0', '4', '1', '6', '5', '7']
From Goal ['7', '10'] ['12', '9', '8', '11', '7', '10']
Path Exists Between start and goal node
'''
