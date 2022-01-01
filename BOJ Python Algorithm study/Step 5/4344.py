C = int(input())

for i in range (C): # case 수만큼 반복
    numbers = list(map(int, input().split())) # 한 case에서 성적, 수 받기
    avg = sum(numbers[1:])/numbers[0]
    count = 0
    for k in range (1, numbers[0]+1):
        if numbers[k]>avg:
            count+=1
    rate = count/numbers[0]*100
    print("%.3f%%" % rate)