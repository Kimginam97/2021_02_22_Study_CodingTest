n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()  # 데이터 정렬

first = data[n - 1]  # 첫번째 큰수
second = data[n - 2]  # 두번째 큰수

# 큰수가 더해야지는 횟수 계산
count = int(m / (k + 1) * k)
count += m % (k + 1)

result = 0
result = count * first
result += (m - count) * second

print(data)
print(result)
