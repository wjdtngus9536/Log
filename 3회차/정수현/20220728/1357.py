# 뒤집힌 덧셈
a,b = input().split()
print("".join(reversed(str(int(a[::-1]) + int(b[::-1])))))