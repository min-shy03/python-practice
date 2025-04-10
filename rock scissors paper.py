# 컴퓨터가 난수를 사용해 가위,바위,보 를 랜덤으로 선택
# 사용자는 가위, 바위, 보중 하나를 선택해 컴퓨터의 선택과 비교하여 승리 여부를 출력하는 프로그램 작성

# 코드 조건
# 사용자 입력은 input() 함수를 통해 받기
# 컴퓨터의 선택은 난수 발생을 이용해 결정 random.choice() 함수 사용
# 사용자와 컴퓨터의 선택 비교 후 승리 여부 출력
# 사용자가 잘못된 입력 시 에러 메세지 출력 후 프로그램 종료

# 코드 작성
# 0. 코드를 작성하기 위해 밑 작업
import random

# 1. 가위바위보 함수 정의
def rockPaperScissors(user) :
    computer = ["가위", "바위", "보"]

    # 2. 사용자에게 가위, 바위, 보 중 하나 입력받기 입력이 잘못 되었다면 에러 메세지 출력 후 종료
    flag = True

    # 사용자가 가위, 바위, 보중 올바른 선택을 했는지 확인
    for char in computer :
        if char == user :
            flag = False
            break

    # 사용자가 올바른 선택을 하지 않았을 시 에러 출력 프로그램 종료
    if flag :
        Error_msg = print("잘못된 입력입니다. 가위, 바위, 보 중에서 선택해주세요")
        return Error_msg

    # 사용자가 올바른 선택을 했을 시 컴퓨터도 가위 바위 보 중 하나를 선택
    else :
        computer = random.choice(computer)

    # 각 상황 별 승리 여부 판단하기
    if user == computer :
        result = "무승부"
    elif (user == "가위" and computer == "보") or (user == "보" and computer == "바위") or (user == "바위" and computer == "가위") :
        result = "승리"
    else :
        result = "패배"
        
    # 승리 여부 판단 후 출력
    if result == "승리" :
        print(f"컴퓨터의 선택 {computer}")  
        print(f"결과 : 당신이 이겼습니다!")
    elif result == "패배" :
        print(f"컴퓨터의 선택 {computer}")  
        print(f"결과 : 당신이 졌습니다!")
    else :
        print(f"컴퓨터의 선택 {computer}")  
        print(f"결과 : 무승부입니다!")

# 함수 호출 후 실행
rockPaperScissors(input("가위,바위,보 중 하나를 선택하세요 : "))