# 행 , 열 값을 받아 온다
n, m = map(int, input().split())

# 결과값 0 으로 초기화
result = 0

# 행을 반복
for i in range(n):
    # 데이터를 리스트로 받아온다
    data = list(map(int, input().split()))
    # n(행)에서 작은 값을 찾아온다
    min_value = min(data)
    # 결과값 과 행에서 작은값을 비교후 큰값을 result 에 넣어 둔다
    result = max(result, min_value)

print(result)