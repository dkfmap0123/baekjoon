n = int(input('인출 인원수 : '))
p = list(map(int, input('사람별 인출 시간({0}개 입력) : '.format(n)).split()))
p.sort()
p2=[]
sum, result = 0

for i in range(n):
    for j in range(0, i+1):
        sum = sum + int(p[j])
    p2.append(sum)
    sum = 0
    result += p2[i]

print(result)
