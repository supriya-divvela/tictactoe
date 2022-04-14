d={'0':['1','2'],'1':['2'],'2':['0','3'],'3':[]}
ol,cl=['0'],['0']
while len(ol):
    t=ol.pop(0)
    for i in d[t]:
        if i not in cl:
            ol.append(i)
            cl.append(i)
print("The path in bfs is:",cl)

'''
output:
The path in bfs is: ['0', '1', '2', '3']
'''
