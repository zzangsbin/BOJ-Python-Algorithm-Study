N = int(input())
score = []
score = list(map(int, input().split()))
# 한 줄로 성적 입력하기
# list는 꼭 앞에 붙여줘야 함!!

size = len(score)
M = max(score)

for i in range (size):
    score[i] = score[i]/M*100

print(sum(score)/size)