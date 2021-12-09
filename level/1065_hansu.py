#각자리수가 등차수열을 이루는걸 한수라고 한다.
# n이 주어지면 1~n까지 한수의 갯수를 출력.

#문자열로 list 나눠받아서 자리별 숫자의 차이가 일정한지 판별
#count

n = int(input('숫자를 입력하시오 : '))
count = 0

for i in range(1, n+1) :
    a = str(i)
    if i<10 :
        count += 1
    elif i>=10:
        min = int(a[0]) - int(a[1])
        for j in range(1, len(a)):
            if int(a[j-1]) - int(a[j]) == min :
                if j == len(a)-1 :
                    count += 1
            else:
                break

print(count)
