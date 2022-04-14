def paths(d,start):
    o,c=[[start]],[[start]]
    while len(o):
        t=o.pop(0)
        for i in d[t[-1]]:
            q=list(t)
            q.append(i)
            if q not in c:
                c.append(q)
                o.append(q)
    return c
g={('s','a'):3,('s','b'):6, ('s','c'):5,('a','d'):9,('a','e'):8,('b','f'):12,('b','g'):14,('c','h'):7,('h','i'):5,('h','j'):6,('i','k'):1,('i','l'):10,('i','m'):2}
d,h={},{}
for i in g.keys():
    if i[-1] not in h.keys():h[i[-1]]=g[i]
for i in g.keys():
    if i[0] not in d.keys():d[i[0]]=[]
    if i[1] not in d.keys():d[i[1]]=[]
    d[i[0]].append(i[1])
start,goal=input().split()
bw=int(input())
h[start]=0
pat=paths(d,start)
if goal not in d.keys():print("Not Possile")
else:
    ol,cl=[(start,0)],[]
    while len(ol):
        ol=sorted(ol,key=lambda x:x[1])[:bw]
        print([i[0] for i in ol],cl)
        t=ol.pop(0)
        if t[0] not in cl:cl.append(t[0])
        if t[0]==goal:
            print([i[0] for i in ol],cl)
            break
        for i in d[t[0]]:
            if i not in cl:ol.append((i,h[i]))]
'''
input:
s i
2
output:
['s'] []
['a', 'c'] ['s']
['c', 'e'] ['s', 'a']
['h', 'e'] ['s', 'a', 'c']
['i', 'j'] ['s', 'a', 'c', 'h']
'''
['j'] ['s', 'a', 'c', 'h', 'i']
