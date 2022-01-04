S = input()
easy = list(set(S))
easy.sort() # 중복되는 것들 다 없애고 리스트로 만듦

count = []
for i in range(26):
    count.append(-1)

for k in range(26):
