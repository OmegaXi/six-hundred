import random 

base = list(range(0,600)) 
for i in range(0,600): 
	base[i] = 0 
for i in range(100000): 
	x = 1200 
	c = list(range(1, 601)) 
	for i in range(599):
		rnum = random.randint(1,x/2) 
		while rnum%2==0: 
			rnum=random.randint(1,x/2) 
		else:
			del(c[rnum-1]) 
			x = x-2 
	base[c[0]-1] = base[c[0]-1] + 1 

for i in range(0,600,10):
	for j in range(0,10):
		print(base[i+j],end="")
	print()

# 600个人，每次随机退出一个奇数位的人
# 最后留下的是谁