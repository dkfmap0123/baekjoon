n = int(input('도시 갯수 (2이상):'))
k = list(map(int, input('도시길이 순서대로 입력 : ').split()))
n_price = list(map(int, input('도시별 주유가격 : ').split()))

#최소가격의 마을 찾기.
min_price = min(n_price)
min_index = n_price.index(min_price)



#나보다 싼 마을이 나오기 전까지의 거리 * 내 주유가격
check = 0
sum=0
distance = 0

for i in range(n):
    if n_price[check] >= n_price[i] :
        print('여기서 멈추자 {0} < {1}'.format(n_price[check], n_price[i]))
        for j in range(check, i):
            distance = distance + k[j]
        sum = sum + distance * n_price[check]
        distance = 0
        check = i

print(sum)
