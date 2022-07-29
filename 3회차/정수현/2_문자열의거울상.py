import sys

sys.stdin = open("_문자열의거울상.txt")

T = int(input())
for i in range(T):
    s = input()
    mirror = ''             # 거울이라는 문자열에 글자마다 해당하는 거울상의 문자로 변형시켜준 뒤 
    for j in s:
        if j == 'b':
            mirror += 'd'
        elif j == 'd':
            mirror += 'b'
        elif j == 'p':
            mirror += 'q'
        elif j == 'q':
            mirror += 'p'
    print(f'#{i+1}',str(mirror[::-1]))  # 문자열 슬라이싱으로 역순으로 변경