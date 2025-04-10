# 야구 게임 만들기
# 컴퓨터가 생성한 중복되지 않는 3개의 난수를 플레이어가 맞추는 게임
# 입력한 숫자와 컴퓨터의 숫자를 비교하여 스트라이크와 볼의 개수 출력

# 요구 조건
# 컴퓨터 난수 생성 - 0~9 까지의 중복되지 않는 정수 3개 생성 randint() 사용
# 키보드를 통해 0~9 까지의 정수 3개 입력
# 예외 처리 XX -> 올바른 입력이 들어왔다는 가정
# 플레이어의 시도가 5번 <= 5 or 스트라이크 아웃 횟수가 2번 이상일 경우 패배
# 플레이어가 컴퓨터 생성 난수값을 자리 순서대로 모두 맞출 경우 승리
# Strike = 자릿수가 같고 "난수 값 == 입력 값" 일 경우
# Ball = 자릿수는 다르지만 입력 값이 난수 값에 포함 될 경우
# Out = 일치하는 숫자가 아무것도 없을 경우

# 코드 작성

# 1. 중복되지 않는 랜덤 정수 3개 생성
import random

while True :
    computer = []
    
    for value in range(3) :
        computer.append(random.randint(0,9))
    
    if computer[0] == computer[1] or computer[1] == computer[2] or computer[0] == computer[2] :
        pass
    else :
        break
            
# 2. 코드에 사용할 변수 생성
count = 1 
out = 0

# 3. 키보드를 통해 0~9의 까지 정수 3개 입력받기
while True :
    
    strike = 0
    ball = 0
    
    # 10. 플레이어의 시도가 5회 초과 시 패배 선언 후 게임 종료
    if count > 5 :
        print("게임 종료 : 패배 (시도 횟수 5회 초과)")
        print(f"정답 : {computer}")
        break
    
    # 키보드를 통해 정수 3개 입력 받기
    user_choose = input(f"시도 {count} : 입력한 숫자 - ")
    
    # 4. 입력 받은 숫자를 정수로 변환 해 리스트에저장
    user_choose_list = list(map(int, user_choose.split(" ")))

    # 5. 입력 받은 숫자가 컴퓨터의 숫자와 일치하는지 확인 
    
    # for 문에서 유저가 선택한 숫자의 위치 변수
    user_choose_location = 0
    
    for value in user_choose_list :
        
        # for 문에서 컴퓨터가 선택한 숫자의 위치
        computer_location = 0
        
        for answer in computer :
            if value == answer :
                # 유저가 선택한 숫자의 위치와 컴퓨터의 숫자 위치가 같으면 스트라이크
                if user_choose_location == computer_location : 
                    strike += 1
                # 답은 맞지만 위치가 다르면 ball 추가
                else :
                    ball += 1
            computer_location += 1
            
        user_choose_location += 1
        
    # 6. 윗 과정을 거치고 아무 것도 검출되지 않았다면 out 추가
    if strike == 0 and ball == 0 :
       out += 1 
    
    # 7. 각 실행별 결과 출력
    print(f"결과 : {strike} Strike, {ball} Ball, {out} Out")
    
    # 8. Strike 일시 정답임으로 게임 종료
    if strike == 3 : 
        print("게임 종료 : 승리")
        print(f"정답 : {computer}")
        break
    # 9. 3 Out 일시 패배임으로 게임 종료
    elif out > 2 :
        print("게임 종료 : 패배 (3 Out)")
        print(f"정답 : {computer}")
        break

    count += 1