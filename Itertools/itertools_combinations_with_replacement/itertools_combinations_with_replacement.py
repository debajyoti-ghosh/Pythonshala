### My solution

from itertools import combinations_with_replacement
list1=[item for item in input().split()]
list1[1]=int(list1[1])
list1[0]=sorted(list1[0])
# l=[]
# for x in range(1,list1[1]+1):  # As upto integer K, not just integer K
t = list(combinations_with_replacement(list1[0],list1[1]))
# l=l+t
# print(t)
z=[''.join(x) for x in t]
print(*z,sep='\n',end='\n')


### Better Solution

import itertools
s = input().split()
string, number = sorted(s[0]), int(s[1])
print(*list(map(''.join, itertools.combinations_with_replacement(string, number))), sep='\n')