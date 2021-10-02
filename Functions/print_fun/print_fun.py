# def print_int(n):
#     int_str=0
#     for candidate in range (1,n+1):
#         if candidate<10:
#             int_str = int_str*10 + candidate
#         elif candidate<100:
#             int_str = int_str*100 +candidate
#         elif candidate<160:
#             int_str = int_str*1000 + candidate

#     return int_str

# n = int(input())
# print("The integer string of n is:", print_int(n))


def print_int(n):
    int_str=[]
    for candidate in range (1,n+1):
        int_str.append(candidate)
    return int_str

n = int(input())
o = print_int(n)
print(*o,sep='',end='\n')
