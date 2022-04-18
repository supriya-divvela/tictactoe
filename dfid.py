d={
    '0':['1','2','3'],
    '1':['3','5'],
    '2':['6'],
    '3':[],
    '4':['5'],
    '5':['4'],
    '6':[]
}
s='0'
g='12'
depth=3 
def dfs(s,g,p,q):
    if p<0:
        return
    q.append(s)
    for i in d[s]:
        if i not in q:
            dfs(i,g,p-1,q)
    return q
for i in range(depth):
    cl=[]
    print(dfs(s,g,i,cl))
'''
output:
['0']
['0', '1', '2', '3']
['0', '1', '3', '5', '2', '6']
'''
