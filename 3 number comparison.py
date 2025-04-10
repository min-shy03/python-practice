# 세 수의 비교 - 유사성과 차이점 찾기

# 사용자로부터 세 개의 정수를 입력 받는다.
# 세 수의 관계의 따라 다음과 같이 출력한다.
# 1. 모든 수가 같으면 "모든 수가 같습니다."
# 2. 두 수가 같으면 "두 수가 같습니다." 
# 3. 모든 수가 다르면 "모든 수가 다릅니다. 가장 큰 수는 x 입니다" 

# 코드 작성

# 1. 사용자로부터 세 개의 정수 입력 받기.
value1 = int(input("첫 번째 수 입력 : "))
value2 = int(input("두 번째 수 입력 : "))
value3 = int(input("세 번째 수 입력 : "))

# 2. 최댓값 찾기
max_num = value1

if max_num < value2 :
    max_num = value2

if max_num < value3 :
    max_num = value3

# 3. 두 수가 같은지 확인
both_num = False
if value1 == value2 :
    both_num = True
    if both_num and value2 != value3 :
        both_num = value1
elif value3 == value2 :
    both_num = True
    if both_num and value1 != value2 :
        both_num = value3
elif value3 == value1 :
    both_num = True
    if both_num and value1 != value2 :
        both_num = value3
        
# . 세 수 비교하기
# 모든 수가 같은지 비교하기
if value1 == value2 == value3 :
    print("모든 수가 같습니다.")
elif value1 != value2 and value2 != value3 and value3 != value1:
    print(f"모든 수가 다릅니다. 가장 큰 수는 {max_num}입니다.")
else : 
    print(f"두 수가 같습니다. 같은 두 수는 {both_num}")
    
    