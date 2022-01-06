numbers = list(input())
numbers.reverse()

num1 = int(numbers[0])*100 + int(numbers[1])*10 + int(numbers[2])
num2 = int(numbers[4])*100 + int(numbers[5])*10 + int(numbers[6])

if num1 > num2:
    print(num1)
else:
    print(num2)