# 로또 시뮬레이션 프로그램 작성

# 요구 사항?
# 1. 로또는 1부터 45까지의 숫자 중 중복되지 않는 랜덤한 숫자 6개를 맞추는 게임의 일종이다.
# 2. 랜덤 수 6개를 전부 다 맞추면 1등, 랜덤 수 5개 보너스 1개를 맞추면 2등, 5개 3등, 4개 4등, 3개 5등이다.
# 3. 사용자가 입력한 숫자의 순서는 상관 없으며 숫자만 맞는다면 된다.
# 4. 사용자는 자동, 수동을 선택할 수 있으며 자동은 6개의 숫자를 대신 선택하고, 수동은 직접 6개의 숫자를 사용자가 고른다.
# 5. 사용자가 선택한 결과를 출력하고 랜덤으로 정해진 번호를 시간 차를 두어 출력한다. (2초 당 한 번호 씩)
# 6. 최종으로 랜덤 7개 숫자와 사용자가 고른 6개 숫자를 출력하여 비교할 수 있도록 하고 등수 결과를 출력한다.


# 코드 알고리즘 작성
# 1. 사용자에게 자동 / 수동 입력 받기 
# 1-1. 자동이라면 랜덤으로 중복되지 않는 6개 숫자를 뽑는다.
# 1-2. 수동이라면 사용자에게 중복되지 않는 6개의 숫자를 입력 받는다. 
# 1-3. 입력을 다 받으면 사용자의 숫자 리스트를 출력한다.

# 2. 랜덤으로 컴퓨터에게 1~45까지의 숫자 중 중복되지 않는 7개의 숫자를 정해둔다. 본 게임 6개 : 보너스 1개

# 3. 사용자의 숫자 리스트와 컴퓨터의 숫자를 비교하여 결과를 계산한다.

# 4. 사용자에게 로또 느낌을 주기위해 시간 차를 두어 컴퓨터가 정한 번호를 한 개씩 출력한다.

# 5. 번호가 다 나온다면 컴퓨터 숫자 리스트, 사용자 숫자 리스트, 결과를 출력한다.

# 코드 작성
import random
import time

def delay() :
    print(".")
    time.sleep(2)
    print(".")
    time.sleep(2)

# 1. 사용자에게 자동, 수동 입력 받기
while True :
    user_choose = input("게임 방식을 선택하세요 (자동 / 수동) : ")
    
    if user_choose == "자동" or user_choose == "수동" :
        break
    else : 
        print("다시 입력하세요.")

# 1-1. 입력 == "자동" 일 경우 1~45 중 중복되지 않는 6개 수 뽑기 
user_num_list = []
if user_choose == "자동" :
    user_num_list = random.sample(range(1,46), 6)

# 1-2. 입력 == "수동" 일 경우 사용자에게 중복되지 않는 6개 수 입력 받기
elif user_choose == "수동" :
    # 중복 확인을 위한 리스트
    check = [0] * 45
    
    # 6개 입력받을 때까지 반복
    while len(user_num_list) < 6 :
        # 사용자에게 현재 선택한 리스트 보여주기
        print(f"현재 선택 한 수 : {user_num_list}")
        user_num = input("1부터 45까지의 수 중 하나를 선택하세요 (중복 X) : ")
        
        # 숫자가 제대로 입력되지 않으면 다시 입력받기.
        if user_num.isdigit() and 1 <=int(user_num) <= 45 :
            user_num = int(user_num)
            # 사용자가 선택한 숫자가 중복되는 걸 방지하기 위해 체크하기
            if check[user_num-1] == 0 :
                user_num_list.append(user_num)
                check[user_num-1] = 1
            else :
                print("중복된 숫자입니다. 다시 입력하세요.")
        else :
            print("잘못 입력되었습니다. 다시 입력하세요.")

# 1-3. 사용자가 선택한 숫자 목록 보여주기
print(f"나의 숫자 : {user_num_list}")

# 예외 - 현실성을 위해 광고 시간 추가
delay()
print("광고중..")
time.sleep(2)
delay()

# 2. 로또 게임 7개의 숫자 선택하기. 본 게임 6개 , 보너스 1개
lotto = random.sample(range(1,46), 7)

# 가장 마지막에 뽑힌 수를 보너스로 한다.
lotto_bonus = lotto[-1]

# 본게임 리스트에서 보너스 숫자를 뺀다.
del lotto[-1]

# 3. 사용자 숫자 리스트와 로또 숫자를 비교한다.
count = 0

for lo in lotto :
    for us in user_num_list :
        if lo == us :
            count += 1

# 3-1. 2등 결과 확인하기 # 디버깅 어케하노..
second_check = 0

if count == 5 :
    if lotto_bonus in user_num_list :
        second_check = 1

# 3-2. 결과 계산
if count == 6 :
    msg = "1등"
elif count == 5 and second_check == 1 :
    msg = "2등"
elif count == 5 :
    msg = "3등"
elif count == 4 :
    msg = "4등"
elif count == 3 :
    msg = "5등"
else :
    msg = "낙첨"

# 4. 로또 번호 사용자에게 보여주기
user_num_list.sort(reverse=False)
lotto.sort(reverse=False)

print("추첨 시작합니다!")
for i in lotto :
    # 2초 간의 간격을 두어 로또 느낌 살리기
    time.sleep(2)
    print(i)
time.sleep(2)
print(f"보너스 번호 : {lotto_bonus}")
time.sleep(2)
delay()

print(f"나의 숫자 : {user_num_list}")
print(f"로또 번호 : {lotto} + {lotto_bonus}")

print(f"맞은 숫자 : {count}개")

if count >= 3 :
    print("축하합니다!")
else :
    print("아쉽네요")

print(f"{msg}입니다.")