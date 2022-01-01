N = int(input())

numbers = []

def arithmetic_numbers():
    for i in range (1, N+1):
        if i<100:
          numbers.append(i)
        elif i<=1000:
            a = i//100 # 백의자리
            b = i%100//10 # 십의자리
            c = i%10 # 일의자리
            if (a-b == b-c):
                numbers.append(i)

    print(len(numbers))

arithmetic_numbers()