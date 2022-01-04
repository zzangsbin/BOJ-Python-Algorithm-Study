N = int(input())
space = ' '
text = '*'

for i in range(N):
    print(space * (N - i - 1) + (text * (i + 1)))