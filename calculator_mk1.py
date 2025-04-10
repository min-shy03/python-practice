# 전역 변수와 지역 변수를 사용한 사칙연산 계산기

# 사용자로부터 초기값을 입력받아 전역 변수로 선언
# 프로그램은 + - * / 중 하나의 연산 수행 가능
# 사용자가 연산을 선택하고 숫자를 입력하면, selectOperation() 함수에서 선택한 연산을 baseValue에 적용
# selectOperation() 함수는 전역 변수 baseValue를 참조하여 연산을 실행
# 나누기 연산에서 분모가 0일 경우, "에러 : 0으로 나눌 수 없습니다." 메세지 출력
# 에러 메세지가 출력되지 않은 경우에만 결과 출력

# 코드 작성
# 1. 사용자로부터 초기값을 입력받기
baseValue = float(input("기본값을 입력하세요 : "))

# 2. 사칙 연산을 수행할 함수 작성
def selectOperation() :
    # 함수 내에서 전역 변수 사용 선언
    global baseValue
    
    while True :
        print("1. 더하기")
        print("2. 빼기")
        print("3. 곱하기")
        print("4. 나누기")

        user_choose = int(input("선택 : "))
        second_value = int(input("숫자 입력 : "))
        
        # 더하기 실행 선택 시
        if user_choose == 1 :
            baseValue = baseValue + second_value
            print("연산 결과 :",baseValue)
            break
        
        # 빼기 실행 선택 시
        elif user_choose == 2 :
            baseValue = baseValue - second_value
            print(baseValue)
            print("연산 결과 :",baseValue)
            break
        
        # 곱하기 실행 선택 시
        elif user_choose == 3 :
            baseValue = baseValue * second_value
            print(baseValue)
            print("연산 결과 :",baseValue)
            break
        
        # 나누기 실행 선택 시 
        elif user_choose == 4 :
            # 나눌 숫자가 0이면 에러 출력
            if second_value == 0 :
                print("Error : 0으로 나눌 수 없습니다.")
                break
            else :
                baseValue = baseValue / second_value
                print("연산 결과 :",baseValue)
                break
            
        # 그 밖의 숫자를 선택할 시 다시 입력
        else :
            print("다시 입력")
            
selectOperation()