N = int(input())

list = list(map(int, input().split()))

# a = [ 3.5, 2.7, 8.5, 4.6 ]
# a = list(map(int, a))
# a = [ 3, 2, 8, 4 ]
# print(a)

print(min(list), max(list))