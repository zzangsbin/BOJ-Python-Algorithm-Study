import sys

T = int(input())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split()) # readline()).split이 아니다.
    print(A + B)