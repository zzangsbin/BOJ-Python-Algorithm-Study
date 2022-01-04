number = int(input())
test = []
for n in range(number):
    test.append(input())

for i in test: # test의 한 원소 즉 XXO... 하나에 대해서
        sum = 0
        count = 0
        for k in i:# XXO... 의 각 문자열에 대해서
            for t in k:
                 if t =='O':
                    count += 1
                    sum += count
                 elif t == 'X':
                    count = 0
        print(sum)