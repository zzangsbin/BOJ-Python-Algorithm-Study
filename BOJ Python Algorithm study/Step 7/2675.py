T = int(input())

for _ in range(T):
    elements = list(map(str, input().split()))
    R = int(elements[0])
    letters = elements[1]
    P = ''
    for i in letters:
        P += i * R
    print(P)