n = input('계산식 입력 (+ - 만 가능): ')
n2 = n[:]

n2 = n2.split('-')
sum=0
sum2 = []

for i in n2:
    n3 = i.split('+')
    for j in n3:
        sum += int(j)
    sum2.append(sum)
    sum=0

print(sum2)
result=sum2[0]
for i in range(1,len(sum2)):
    result -= sum2[i]
print(result)
