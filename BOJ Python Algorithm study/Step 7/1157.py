letter = input()
Big = letter.upper()
all = list(set(Big))

A = []

for i in all:
    count = 0
    for k in Big:
        if i==k:
            count+=1
    A.append(count)

for t in range (len(A)):
    if A.count(max(A))>=2:
        print('?')
        break
    else:
        if A[t]==max(A):
            print(all[t])