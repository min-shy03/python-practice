# 주사위 던지기 결과의 빈도를 분석하고, 히스토그램? 을 통해 결과를 시각화

# 구현 내용
# 1. 사용자로부터 주사위를 던질 횟수를 입력 받는다 (100~1,000,000 사이) 유효하지 않으면 재입력
# 2. 사용자가 입력한 횟수 만큼 주사위 던지기 주사위의 결과는 1부터 6 사이의 숫자다 각 숫자의 발생 횟수를 카운트 한다.
# 3. 각 숫자의 발생 횟수를 히스토그램으로 시각화 한다. 각 *은 최대치에 대한 상대적인 비율로 나타낸다. 최대 10개
# 3-1. *의 갯수 =  각 숫자 시행 횟수 / 가장 많이 실행된 숫자의 횟수 * 10 

# 코드 작성
import random

# 1. 사용자에게 횟수 입력 받기 100 ~ 1,000,000 사이가 아니면 오류 출력
while True : 
    dice_count = int(input("주사위를 몇 번 굴릴지 입력하세요 : "))
    
    if 100 <= dice_count <= 1000000 :
        break
    else :
        print("범위를 벗어났습니다. 다시 입력하세요. ")
        pass

# 2. 사용자가 정한 입력 횟수만큼 주사위를 랜덤으로 돌린 후 각각의 결과를 카운트한다.
# 각각의 결과를 담을 변수
count = [0,0,0,0,0,0]

# 주사위 돌린 후 각각의 결과 카운팅 하기
for i in range(dice_count) :
    rand_value = random.randint(1,6)
    
    # 쓸데없이 if문을 늘리는 것이 아닌 각각의 값에 1씩 추가 -> 코드 사고력을 늘리기 ★ 챗지피티 도움 받음
    count[rand_value-1] += 1
    
    # if rand_value == 1 :
    #     count[0] += 1
    # elif rand_value == 2 :
    #     count[1] += 1
    # elif rand_value == 3 :
    #     count[2] += 1
    # elif rand_value == 4 :
    #     count[3] += 1
    # elif rand_value == 5 :
    #     count[4] += 1
    # else :
    #     count[5] += 1
        

# 최대 실행 횟수 찾기
max_num = count[0]

if max_num < count[1] :
    max_num = count[1]
    
if max_num < count[2] :
    max_num = count[2]
    
if max_num < count[3] :
    max_num = count[3]
    
if max_num < count[4] :
    max_num = count[4]
    
if max_num < count[5] :
    max_num = count[5]

# 각 평균과 히스토그램 담을 리스트 변수 생성
avg = [0, 0, 0, 0, 0, 0]
star = ["", "", "", "", "", ""]


# 각각의 결과를 리스트에 담기 
for i in range(6) :
    avg[i] = (count[i] / dice_count) * 100
    star[i] = "*" * int(count[i] / max_num * 10)

# 결과 출력
print("주사위 시행 결과 출력")
for i in range(6) :
    print(f"{i+1} : {star[i]} ({count[i]} times, {avg[i]}%)")