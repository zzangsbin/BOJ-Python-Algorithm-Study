N = int(input())
numbers = input()
sum = 0
for i in range(N):
    sum += int(numbers[i])

print(sum)

# result = sum(int(numbers[0:]))numbers 왜 이건 안 되는지?