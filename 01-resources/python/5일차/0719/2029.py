import sys
sys.stdin = open('input.txt', 'r')
T = int(input())

for i in range(1, T+1):
    a,b=map(int, input().split())
    print('#%d %d %d'%(i, a//b, a%b))
