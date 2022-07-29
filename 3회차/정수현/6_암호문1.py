import sys

sys.stdin = open("_암호문1.txt")

for t in range(10):

    N = int(input())                            # 원본 암호문 길이 
    origin = list(map(int, input().split()))    # 원본 암호문
    n = int(input())                            # 명렁 개수
    orders = list(input().split())              # 암호화 명령
    
    order = 0
    i = 0
    while order < n:
        if orders[i] == 'I':            # split('I')를 기준으로 새로운 변수에 명령어들을 분해해서 넣을 수 있지만 변수를 절약해 보았다.
            x = int(orders[i+1])
            y = int(orders[i+2])
            for j in range(y):
                try:                    # list index out of range 에러의 경우도 고려해 보았다.
                    origin.insert(x + j, int(orders[i+3 + j]))
                except:
                    origin.append(int(orders[i+3 + j]))
            i += 3 + y                  # 명령어당 필요한 index값을 계산하여 건너뛰어 준다. (하드코딩인가?..)
            order += 1
    print('#%d %s'%(t+1, ' '.join(map(str, origin[0:10])))) # 문자열 join함수를 통해 출력 포멧을 맞춰 주었다.
