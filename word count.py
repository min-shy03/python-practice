# 사용자에게 문자열을 입력받고 원하는 특정 단어의 빈도를 계산하는 프로그램

# 코드 작성

# 사용자에게 문자열 입력 받기
word = input("문자열 입력 : ")
temp = ""
# 빈도 측정 변수
count = 0

# 유저가 찾기를 원하는 단어
user_word = input("단어 입력 : ")

# 마지막 단어 판별을 위해 문장 마지막에 공백 추가
word += " " 

for i in word :
    # 문자열이 띄어쓰기가 입력되면 추가를 멈추고 temp에 담긴 문장이 user_word랑 같은지 판별 
    if i == " " :
        if temp == user_word :
            count += 1
            temp = ""
        else :
            temp = ""
    # 띄어쓰기가 나올 때 까지 문자열을 temp 임의 변수에 하나씩 저장
    else :
        temp += i
        
    # 문자열이 더해지면서 유저가 원하는 단어가 나오면 카운트 1업 및 리셋
    

print(f"단어 출현 빈도 : {count}회")