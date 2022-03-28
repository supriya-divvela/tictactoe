import sys
def man(m,p,q,s):
    r=0
    flag=False
    for i in range(u):
        for j in range(w):
            if m==s[i][j]:
                flag=True
                r+=abs(p-i)+abs(q-j)
                break
        if flag==True:break
    return r
    
def pos(s,l):
   c=0
   for i in range(u):
      for j in range(w):
          if l[i][j]!=s[i][j]:
            c+=man(l[i][j],i,j,s)
   return c
def fun(temp1,m,n):
   t=[]
   if 0<=m+1<=(u-1) and 0<=n<=(w-1):
      temp=[list(i) for i in temp1]
      temp[m][n],temp[m+1][n]=temp[m+1][n],temp[m][n]
      t.append(temp)
   if 0<=m<=(u-1) and 0<=n+1<=(w-1):
      temp=[list(i) for i in temp1]
      temp[m][n],temp[m][n+1]=temp[m][n+1],temp[m][n]
      t.append(temp)
   if 0<=m-1<=(u-1) and 0<=n<=(w-1): 
      temp=[list(i) for i in temp1]
      temp[m][n],temp[m-1][n]=temp[m-1][n],temp[m][n]
      t.append(temp)
   if 0<=m<=(u-1) and 0<=n-1<=(w-1): 
      temp=[list(i) for i in temp1]
      temp[m][n],temp[m][n-1]=temp[m][n-1],temp[m][n]
      t.append(temp)
   return t

u=int(input("Enter number of rows:"))
w=int(input("Enter number of columns:"))
l=[[int(x) for x in input().split()] for i in range(u)]
z=[[int(x) for x in input().split()] for i in range(u)]
temp=[list(i) for i in l]
v=[(temp,pos(z,temp))]
q=[(temp,pos(z,temp))]
flag=False
while 1:
    if q!=[]:
       m=sorted(q,key=lambda x:x[1])[0][1]
       q=list(filter(lambda x:x[1]==m,q))
       d=q.copy()
       q=[]
       while len(d):
           temp3=d.pop(0)
           for i in range(u):
              if 0 in temp3[0][i]:
                 x=i
                 y=temp3[0][i].index(0)
                 break
           temp2=fun(temp3[0],x,y)
           for i in temp2:
              if i not in [x[0] for x in v]:
                  if i==z:
                     print(i,"Found")
                     sys.exit(0)
                  elif pos(z,i)>max([x[1] for x in v]):
                      pass
                  else:
                     v.append((i,pos(z,i)))
                     q.append((i,pos(z,i)))
    else:
        print("Not Possible")
        break
'''
input:
Enter number of rows:3
Enter number of columns:3
1 2 3
5 6 0
7 8 4
1 2 3
5 8 6
0 7 4
output:
Found
'''
