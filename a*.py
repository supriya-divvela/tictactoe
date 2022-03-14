def distance(m):
    y=0
    for i in range(len(m)-1):
        if (m[i],m[i+1]) in d:
            y+=d[(m[i],m[i+1])]
        if (m[i+1],m[i]) in d:
            y+=d[(m[i+1],m[i])]
    y+=h[m[-1]]
    return y
    
def paths(l,start,goal):
    o,c=[[start]],[[start]]
    while len(o):
        t=o.pop(0)
        for i in p[t[-1]]:
            if i not in list(t):
                q=list(t)
                q.append(i)
                c.append(q)
                o.append(q)
    return c

p={
    's':['a','d'],
    'a':['s','d','b'],
    'b':['a','e','c'],
    'e':['d','b','f'],
    'f':['e','g'],
    'g':['f'],
    'c':['b'],
    'd':['s','a','e']
}
d={('s','a'):3,
    ('s','d'):4,
    ('a','d'):5,
    ('a','b'):4,
    ('d','e'):2,
    ('b','e'):5,
    ('b','c'):4,
    ('e','f'):4,
    ('f','g'):3.5
}
h={'s':11.5,'a':10.1,'b':5.8,'c':3.4,'d':9.2,'e':7.1,'f':3.5,'g':0}
v=paths(p,'s','g')
k=list(filter(lambda x:x[-1]=='g',v))
r=[]
for i in k:
    z=distance(i)
    r.append((i,z))
r=sorted(r,key=lambda x:x[1])
print(f"The Path and distance is {r[0][0]} and {r[0][1]}")

'''
output:The Path and distance is ['s', 'd', 'e', 'f', 'g'] and 13.5
'''
