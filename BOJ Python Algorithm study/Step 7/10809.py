S = input()
ascii = []
for i in range(26):
    ascii.append(-1)

for k in range(len(S)):
    if ascii[ord(S[k])-97] == -1:
        ascii[ord(S[k])-97] = k

for j in range(26):
    print(ascii[j], end =' ')