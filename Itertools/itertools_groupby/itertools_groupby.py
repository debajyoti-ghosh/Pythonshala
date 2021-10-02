from itertools import groupby
list1= input().split()
print(list1)
# t = list(groupby(list1[0],None))
print(*[(int(c),len(list(cs))) for c,cs in (list1[0])])
# z=[''.join(x) for x in l]
# print(*z,sep='\n',end='\n')
