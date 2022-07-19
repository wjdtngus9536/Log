T = int(input())
s = 0
while T:
    s += T%10
    T=T//10

print(s)