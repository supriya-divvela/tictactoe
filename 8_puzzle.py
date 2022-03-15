def pos(s,l):
   c=0
   for i in range(3):
      for j in range(3):
         if l[i][j]!=s[i][j]:
            c+=1
   return c
def fun(temp1,m,n):
   t=[]
   if 0<=m+1<=2 and 0<=n<=2:
      temp=[list(i) for i in temp1]
      temp[m][n],temp[m+1][n]=temp[m+1][n],temp[m][n]
      t.append(temp)
   if 0<=m<=2 and 0<=n+1<=2:
      temp=[list(i) for i in temp1]
      temp[m][n],temp[m][n+1]=temp[m][n+1],temp[m][n]
      t.append(temp)
   if 0<=m-1<=2 and 0<=n<=2: 
      temp=[list(i) for i in temp1]
      temp[m][n],temp[m-1][n]=temp[m-1][n],temp[m][n]
      t.append(temp)
   if 0<=m<=2 and 0<=n-1<=2: 
      temp=[list(i) for i in temp1]
      temp[m][n],temp[m][n-1]=temp[m][n-1],temp[m][n]
      t.append(temp)
   return t
   
l=[[int(x) for x in input().split()] for i in range(3)]
z=[[int(x) for x in input().split()] for i in range(3)]
temp=[list(i) for i in l]
v=[temp]
q=[temp]
flag=False
while(len(q)):
   temp=q.pop(0)
   if temp==z:
      flag=True
      print(True)
      break
   for i in range(3):
      if 0 in temp[i]:
         x=i
         y=temp[i].index(0)
         break
   temp2=fun(temp,x,y)
   '''m=[]
   for i in temp2:
      m.append((i,pos(i,z)))
   m=[i[0] for i in list(filter(lambda x:x[1]==sorted(m,key=lambda x:x[1])[0][1],m))]'''
   for i in temp2:
      if i not in v:
         v.append(i)
         q.append(i)
if flag==False:
   print("not Possible")
    
    
'''
input:
1 2 3
5 6 0
7 8 4
1 2 3
5 8 6
0 7 4
output:
True
input:
1 2 3
8 0 4
7 6 5
2 8 1
0 4 3
7 6 5
output:
True
'''
