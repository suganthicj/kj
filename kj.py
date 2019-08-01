x11=int(input())
l=list(map(int,input().split()))
u11=0
z11=1
m=0
for p in range(x11-1):
	if l[p]<l[p+1] and u11==0 :
		u11=1
		z11+=1 
		if z11>m:
			m=z11
	elif l[p]<l[p+1] and u11==1:
		z11+=1
		if z11>m:
			m=z11
	elif l[p]>l[p+1] and u11==1:
		u11=0
		z11=1
	else:
