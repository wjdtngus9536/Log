a = int(input())
r=0
while a:
    r*=10
    r+=a%10
    a//=10
print(r)