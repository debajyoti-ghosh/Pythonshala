from itertools import permutations
list1=[item for item in input().split()]
# permu_len = list1[1]
list1[1]=int(list1[1])
# o = tuple(list1)
# print(o)
t = list(permutations(list1[0],list1[1]))
print(t)
t.sort()
z=[''.join(x) for x in t]
print(*z,sep='\n',end='\n')
# print(permu_len)