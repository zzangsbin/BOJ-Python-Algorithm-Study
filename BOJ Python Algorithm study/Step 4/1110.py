N = int(input())
n = N
i = 0 # 사이클 횟수

while (True):
    n = (n%10)*10 + (n//10 + n%10)%10
    i=i+1
    if (n==N):
        break

print(i)