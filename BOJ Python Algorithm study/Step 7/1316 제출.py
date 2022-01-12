N = int(input())
count = N

for _ in range(N):
    letters = input()
    for i in range(len(letters) - 1):
        if letters[i] !=  letters[i + 1]:
            if letters[i] in letters[i + 1:]:
                count -= 1
                break

print(count)