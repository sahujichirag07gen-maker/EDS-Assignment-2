# 2.2.2 Captain of the team 
ht=list(map(int, input().split()))
maxheight=ht[0]
e=0
for e in ht:
	if(maxheight<e):
		maxheight=e
print(maxheight)