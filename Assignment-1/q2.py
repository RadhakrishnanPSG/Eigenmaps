from math import sqrt
n = int(input())
cnt = 0
if n%2==1:
    for i in range(1,int(sqrt(n))+1,2):
        if n%i==0:
            if (n/i)%2==1:
                cnt+=1
else:
    for i in range(2,int(sqrt(n))+1,2):
        if n%i==0:
            if (n/i)%2==0:
                cnt+=1
print(cnt)
