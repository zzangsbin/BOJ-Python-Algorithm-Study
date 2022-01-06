# def solution(participant, completion):
#     part = set(participant)
#     comp = set(completion)
#     result = list(part-comp)
#     answer = print(""%d"" % result)
#     return answer
#


def solution(participant, completion):
    answer = ''
    for i in participant:
        if i not in completion:
            answer = "\"" + i + "\""
        print(answer)
        break


solution(["leo", "kiki", "eden"], ["eden", "kiki"])