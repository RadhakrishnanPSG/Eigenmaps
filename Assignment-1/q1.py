import math
n,m = map(int,input().split())
groups = list(map(int,input().split()))

planes = list(map(int,input().split()))
groups.sort(reverse=True)
planes.sort(reverse=True)

if max(groups) > max(planes):
    print(-1)
else:
    trips = math.ceil(sum(groups) / min(planes))
    time = (trips - 1) * 2 + 1
    print(time)
