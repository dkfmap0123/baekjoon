#최소횟수로 30씩 더해서 없애라

n = int(input('기프티콘 갯수 : '))
A = list(map(int, input('기프티콘별 남은 기한:').split()))
B = list(map(int, input('기프티콘 며칠뒤 사용할것인지 : ').split()))

#최소횟수로 시간의 흐름에 맞춰 A>=B 만들기.
count = 0
min_a = min(A)
max_b = max(B)
while max_b != 0:

    for i in range(n):
        A[i] -= min_a
        B[i] -= min_a

    A = list(map(lambda x:x+30, A))
    count += 1

    for i in range(n):
        if A[i] >= B[i]:
            B[i] = 0
            max_b = max(B)

        else:
            B[i] -= A[i]
            count += 1

    min_a = min(A)

print(count)
