d={'0':['1','2','3'],'1':['0','2'],'2':['0','1','4'],'3':['0'],'4':['2']}
cl,start=[],'0'
def dfs(p,cl):
    cl.append(p)
    for i in d[p]:
        if i not in cl:
            dfs(i,cl)
    return cl
print("The path in bfs is:",dfs(start,cl))

'''
output:
The path in dfs is: ['0', '1', '2', '4', '3']
'''
