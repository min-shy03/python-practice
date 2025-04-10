import random

word_list = []

def input_word() : 
    count = 1
    # 단어 리스트가 3개가 될때까지반복
    while len(word_list) < 3 :
        msg = input(f"{count}번째 단어를 입력 하세요 : ")
        
        if 5 <= len(msg) <= 20 :
            word_list.append(msg)
            count += 1
        # 단어가 짧거나 길면 오류 출력
        else :
            print("5글자 이상 20이하 글자로 구성된 단어를 입력하세요.")
    
    rand_word = random.choice(word_list)
    
    # 랜덤으로 선택된 단어 문자열을 반환값으로 설정
    return rand_word

def rand_blind(rand_word) :
     # 랜덤으로 선택된 단어가 짝수 개일 경우 50%만큼 블라인드 처리
    if len(rand_word) % 2 == 0 :
        blind_count = int(len(rand_word) / 2)
    # 홀수 개일 경우 반올림 처리 
    else :
        blind_count = int(len(rand_word) / 2) + 1
    
    # 문자열을 블라인드로 바꿔 처리하기 위해 리스트형태로 전환
    rand_word_listform = [i for i in rand_word]
    
    # 위에서 구한 블라인드 처리 갯수 만큼 단어 블라인드
    for i in range(blind_count) :
        while True :
            rand_count = random.randint(0, len(rand_word_listform)-1)
            # 블라인드 처리될 부분이 중복처리 될 수도 있음으로 계속 반복처리
            if rand_word_listform[rand_count] != "_" :
                rand_word_listform[rand_count] = "_"
                break
            else :
                pass
    
    # 블라이드 처리 된 리스트 형태의 단어를 함수 반환값 설정
    return rand_word_listform

rand_word = input_word()
rand_blind_listform = rand_blind(rand_word)

# 게임 구현 코드
print(f"단어 선택 완료 게임을 시작합니다.")

# 유저의 시도 횟수를 세어 담는 변수 생성
count = 1

while True :
    print("=========================================================================")
    print(f"{count}번째 시도, 아래 단어를 구성하는 알파벳을 한 개 입력하세요.")
    print("".join(rand_blind_listform))
    
    while True :
        user_choose = input("알파벳 입력 : ")
        
        if len(user_choose) > 1 :
            print("한 개만 입력하세요.")
        else :
            break
            
    alphabet_check = False
    word_location = 0
            
    # 랜덤 문자에서 하나씩 받아온 후 유저가 선택한 알파벳과 맞으면 리스트 내 언더 바 수정.
    for i in rand_word :
        if user_choose == i :  
            rand_blind_listform[word_location] = i
            # 유저가 선택 한 알파벳이 단어내에 있으면 체크
            alphabet_check = True
        else :
            pass
                
        word_location += 1
            
    # 체크가 False면 알파벳이 하나도 없었다는 뜻
    if alphabet_check == False :
        print("=========================================================================")
        print("일치하는 알파벳 없음") 
            
            
    # 사용자가 모든 알파벳을 맞췄는지 확인
    answer_check = True
    for i in rand_blind_listform :
        if i == "_" :
            answer_check = False
            
    # 모든 알파벳을 맞췄으면 게임 종료
    if answer_check == True :
        print("=========================================================================")
        print(f"Clear - 선택된 단어 : {rand_word}, 총 시도 횟수 : {count}")
        break
            
    count += 1
