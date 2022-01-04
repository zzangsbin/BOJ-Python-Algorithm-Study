# numbers = list(map(int, input().split()))
# 이건 한줄로 받기!

numbers = []
for i in range(9):
    # num = int(input())
    # numbers.append(num)
    numbers.append(int(input()))

order = 0

maximum = max(numbers)

for i in range(9):
    if maximum == numbers[i]:
        order = i + 1
        break

# for i in numbers:
#     if maximum == numbers[i]: 가 아님.
#         order = i+1
#         break

print(maximum, order)
