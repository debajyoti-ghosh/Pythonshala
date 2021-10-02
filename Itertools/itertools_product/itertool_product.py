from typing import ChainMap


from itertools import chain, repeat, product
list1 = []
list2 = []
list1 = [int(item) for item in input("Enter item of 1st list:").split()]
list1.sort()
print(list1)
# list2 = [int(item) for item in input("Enter item of 2nd list:").split()]
# list2.sort()
# final_list=list((list1,list2))

# print(final_list)
# print(list(product(*final_list)))