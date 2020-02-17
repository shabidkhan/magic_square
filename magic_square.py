marks = [
    [1, 0, 4, 8],
    [0, 2, 0, 6],
    [2, 4, 5, 2],
    [9, 5, 8, 3]
]
d1=0
d2=0
c=[]
r=[]
for i in range(len(marks)):
	r.append(0)
	for j in range(len(marks)):
		c.append(0)
		if(i==j):
			d1=marks[i][j]+d1
		if (i+j==len(marks)-1):
			d2+=marks[i][j]
		r[i]+=marks[i][j]	
		c[j]+=marks[i][j]
	print('r',i,'=',r[i])
	print('c',i,'=',c[i])
print('d1=',d1)
print('d2=',d2)
