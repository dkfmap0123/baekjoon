#셀프넘버가 아닌걸 리스트에 모으고
#1~10000중에서 빼버리기
min_num = []
result = []

for i in range(1, 10000):
    A=str(i)
    sum = 0
    sum += i
    for j in range(len(A)):
        sum = sum + int(A[j])
    min_num.append(sum)

min_num = set(min_num) #중복제거
min_num = sorted(min_num) #set 사용시 순서가 꼬이기때문에 다시 정렬

for i in range(1, 10000):
    if i in min_num:
        min_num.remove(i)
    else:
        result.append(i)

print(result[:10], end='...')
print(result[-5:])
