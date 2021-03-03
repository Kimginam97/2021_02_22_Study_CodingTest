# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])

# ord 는 아스키 값을 돌려준다 a = 97
column = int(ord(input_data[0]))-int(ord('a'))+1


# 나이트가 이동할수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각위치로 이동 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]

    # 해당위치로 이동이 가능하다면 카운트 증가
    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        result += 1

print(result)
