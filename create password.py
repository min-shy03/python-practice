# 사용자로부터 길이를 입력 받아 해당 길이의 무작위 패스워드를 생성하는 함수 구현
# 이 함수는 대문자, 소문자, 숫자를 조합하여 패스워드를 생성해야 합니다.

# 코드 조건
# 패스워드 생성에는 random.choice() 함수 사용
# 패스워드는 대문자(A-Z), 소문자(a-z), 숫자(0-9)를 랜덤하게 포함해야 함
# 함수 내에서 직접 input 함수를 사용하여 사용자에게 길이를 입력받지 않는다
# 생성된 패스워드는 문자열로 반환해야 한다

# 코드 작성
# 0. 코드를 작성하기 위해 random 모듈 import
import random

# 1. 함수 작성
def generate_password(length) :
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = upper.lower()
    num = "123456789"
    
    all_char = upper + lower + num
    
    # 대문자, 소문자, 숫자가 하나씩 잘 들어갔는지 확인 절차 후 없으면 될 때까지 재생성
    while True :
        count = 0
        password = ""
        for i in range(length) :
            password += random.choice(all_char)
        
        # 대문자 확인
        for char in password :
            if char.isupper() :
                count += 1
                break
        
        # 소문자 확인
        for char in password :
            if char.islower() :
                count += 1
                break
        
        # 숫자 확인
        for char in password :
            if char.isdigit() :
                count += 1
                break
        
        # 위의 조건들을 모두 만족할 시 반복 종료
        if count == 3 :
            break
                
    return password

# 3. 함수 호출 후 실행 결과 확인
print(generate_password(int(input("랜덤으로 생성할 문자열 길이 입력 : "))))