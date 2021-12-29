numbers = []

for i in range (10):
    numbers.append(int(input()))

for k in range (10):
    numbers[k] = numbers[k]%42 # i 아니고 k!!!!!

numbers = list(set(numbers))

# print(numbers)
size = len(numbers)
print(size)