N = int(input())
count = N

# for _ in range(N):
#     L = input()
#     for i in range(len(L) - 1):
#         if L[i] != L[i + 1]:
#             if L[i] in L[i + 1:]:
#                 pass
#             else:
#                 if i == len(L) - 1:
#                     count += 1
#                 else:
#                     continue
#         else:
#             count += 1

for _ in range(N):
    l = input()
    for i in range(len(l) - 1):
        if l[i] !=  l[i + 1]:
            if l[i] in l[i + 1:]:
                count -= 1
                break

print(count)