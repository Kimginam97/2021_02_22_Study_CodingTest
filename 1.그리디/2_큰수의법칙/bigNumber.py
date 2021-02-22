n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()  # 데이터 정렬

first = data[n - 1]  # 첫번째 큰수
second = data[n - 2]  # 두번째 큰수

result = 0

while True:
    for i in range(k):  # 가증 큰수를 K번 더하기
        if m == 0:  # m 이 0 이면 반복문 탈출
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)
