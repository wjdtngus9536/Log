import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for i in range(1, T+1):
    print('#%d %.0f'%(i, sum(map(int, input().split()))/10))