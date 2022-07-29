import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())
for i in range(T):
    N = int(input())
    incomes = list(map(int, input().split()))
    average = sum(incomes)/N                    # int로 이뤄진 소득액 리스트(incomes)의 평균값을 구하고
    cnt = 0
    for j in incomes:
        if j <= average:
            cnt += 1                            # 평균보다 낮은 사람의 수를 센다.
    print('#{} {}'.format(i+1, cnt))
