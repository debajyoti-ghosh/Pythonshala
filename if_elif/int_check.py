# if __name__ == '__main__':
#     n = int(input().strip())
# print("Weird") if (6<=n<=20 or n % 2 !=0) else print(" Not Weird")

if __name__ == '__main__':
    n = int(input().strip())
print("Leap Year") if ((n%4==0 and n%100 !=0) or (n%100==0 and n%400 ==0)) else print(" Normal Year")

