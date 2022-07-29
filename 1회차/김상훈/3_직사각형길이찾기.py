import sys
sys.stdin = open("_직사각형길이찾기.txt")

# d 를 구한다고 가정
# d = (3개의 수에서 마주보는 변끼리 빼고 나머지 하나를 더하면 됨 )
# a와 b가 다를 때 d = a 또는 b 이고, c = a 또는 b 임
#
# a = 

# c와 d가 다를 때  c는 a 또는 b와 같고  a는 c 또는 d와 같다.

rec = []
T = int(input())
for _ in range(0,T):
    a,b,c = map(int,input().split())
    if a != b : # 이 경우 d는 a 와 b 중 하나랑 마주봄 c 역시 a 또는 b 와 마주봄.
        d = a - c + b
    else : # b = c 면 (정사각형 인 경우)
        d = c
    rec.append(d)
for i in range(1,T+1):
    print(f'#{i} {rec[i-1]}')
    
    