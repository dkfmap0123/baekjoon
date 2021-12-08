if __name__ == '__main__':
    n, k = map(int, input('동전의 갯수 N과 내가 만들려는 금액 K를 입력해주세요').split(' '))
    A=[]
    B=[]

    for i in range (0, n):
        A.append(input('동전 금액 입력해주세요 ({0}/{1}))'.format(i+1,n)))



    for i in A:
        print(i, end='\n')

    A.reverse()
    A = map(int, A)
    my_sum = 0
    for i in A:
        if k//i > 0:
            count = 0
            count += k//i
            my_sum += count
            k %= i
            B.append('{0}*{1}'.format(i,count))
            if k<=0:
                break

    print('필요한 동전 갯수 {0}'.format(my_sum))
    print('필요 동전 종류 {0}'.format(B))

