# 자연수 N에 대한 가장 작은 생성자를 구하라
# 생성자가 없는 경우에는 0을 반환하라

N = int(input())
flag = False
# 18미만의 숫자의 경우 N - 자리수 * 9를 시작점으로 잡게 되면 바운더리를 벗어나게 되므로 case를 나눔으로써
# 그냥 1부터 생성자를 찾는 경우 1388ms 였던 시간을 72 ms로 단축할 수 있게 되었다.
# N이 아무리 커져도 for문의 반복 수는 자릿수*9를 넘지 않으므로
# O(n) -> O(d)으로 시간 복잡도를 대폭 줄일 수 있었다.
if N > 18:
    start = N - 9 * len(str(N))
else:
    start = 1

for i in range(start, N+1):
    if N == i + sum(list(map(int, str(i)))):
        print(i)
        flag = True
        break

if flag == False:
    print(0)    