A = int(input())
B = int(input())
C = int(input())

result = str(A * B * C)

# print(result+"입니다")

for i in range(10):
    count = 0
    for k in result:
        if str(i) == k:
            count = count + 1
    print(count)
