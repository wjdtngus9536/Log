import sys

sys.stdin = open("_직사각형길이찾기.txt")

# 홀수인 길이에 해당하는 길이가 필요함.
T = int(input())
for i in range(T):
    tc = map(int, input().split())
    re = {}
    for j in tc:
        if re.get(j):
            re[j] += 1
        else:
            re[j] = 1
    for k in re:
        if re[k] % 2 == 1:
            print(f'#{i+1}', k)
