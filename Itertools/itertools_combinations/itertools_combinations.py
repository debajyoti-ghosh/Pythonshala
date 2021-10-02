from itertools import combinations
list1=[item for item in input().split()]
list1[1]=int(list1[1])
list1[0]=sorted(list1[0])
l=[]
print(type(l))
for x in range(1,list1[1]+1):  # As upto integer K, not just integer K
    t = list(combinations(list1[0],(x)))
    l=l+t
print(l)
z=[''.join(x) for x in l]
print(*z,sep='\n',end='\n')
