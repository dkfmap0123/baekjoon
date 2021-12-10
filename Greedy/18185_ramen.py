#n개의 라면공장
#i번공장에서 A개의 라면 구매

#최소의 비용으로 라면을 구매하고자 한다.
#i / i+1 / i+2 1개씩 3개 구매시 7

n = int(input('라면 공장 갯수 : '))
A = list(map(int, input('공장당 구매하려는 갯수').split()))

#연속적으로 구매할 수 있는게 최선. (3 / 5 / 7)
sum=0
for i in range(n):
    while A[i]>0:
        if i+1<n and A[i+1]>0 :
            if i+2<n and A[i+2]>0:
                sum += 7
                A[i] -= 1
                A[i+1] -= 1
                A[i+2] -= 1
            else:
                sum += 5
                A[i] -= 1
                A[i+1] -= 1

        else:
            sum += 3
            A[i] -= 1

print(sum)
