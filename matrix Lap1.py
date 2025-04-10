# 사용자로부터 start , End , N 세 값을 입력 받는다
# 이 값을 사용하여 start , end 사이의 중복 되지 않은 n개 난수 생성 후 1차원 리스트에 저장

# 코드 조건
# 1. Start - 0 이상, End 보다 작아야 함
# 2. End - Start 보다 커야함
# 3. N - Start , End 사이 가능한 최대 수 이하

# 요구 사항
# 1. 입력 조건이 유효할 때까지 재입력 요구
# 2. 리스트 출력

# 코드 작성

# 1. 사용자로부터 Start 값 입력받기 - 0 이상 
import random

print("난수를 생성할 범위와 개수를 입력하세요.")

while True :
    start = int(input("Start (0 이상의 정수) : "))
    # Start 입력 값이 0보다 작으면 다시 입력 받기
    if start < 0 : 
        print("Start 값은 0보다 커야 합니다.")
    else :
        break
    
# 2. End 값 입력 받기
while True :
    end = int(input("End (Start 초과 정수) : "))
    # End 입력 값이 Start 보다 작거나 같으면 다시 입력 받기
    if end <= start : 
        print("End 값은 Start보다 커야 합니다.")
    else :
        break
    
max_num = (end - start + 1)    
    
# 난수 발생 횟수 입력 받기
while True :
    rand_count = int(input("N (생성 할 난수 개수) : "))
    # 난수 생성 최대 값보다 입력값이 크면 다시 입력 받기
    if max_num < rand_count  : 
        print(f"N은 {start}부터 {end} 사이의 정수여야 합니다.")
    else :
        break

# 숫자 담을 리스트 생성
num_list = []

# N값 만큼 난수 생성
for _ in range(rand_count) :
    num_list.append(random.randint(start, end))

# 중복 검사
for i in range(rand_count) :
    while True :
        # count() 함수 - 리스트에 특정 요소가 몇 개 있는지 세어주는 함수 중복 검사시 유용하게 활용 가능
        if num_list.count(num_list[i]) > 1 :
            num_list[i] = random.randint(start, end)
        else :
            break

print("생성된 난수 리스트 : ")
print(num_list)


# 코드 개선점 - CONTINUE 를 이용해 입력 받을 줄을 현저하게 줄일 수 있다. 중복 검사는 random.sample을 이용하면 편하게 할수 있다.