# 빙고 게임 프로그램 작성

# 알고리즘 작성
# 1. 사용자로부터 3 <= N <= 6 인 N 값을 정수로 입력 받는다. 유효하지 않으면 재입력 무한 반복 -> while 사용
# 2. 빙고 보드생성 N x N 크기의 빙고 보드를 위해 1차원 리스트 생성. 이 리스트는 1 ~ 36 사이의 중복되지 않은 정수로 채움.
# 3. 생성된 리스트를 사용하여 N x N 형태의 빙고 보드를 출력
# 4. 사용자가 엔터 키를 누르면 1 ~ 36 사이 난수 발생 시키고 화면에 출력 -> 살짝 이해 안됨 ?? 
# 5. 보드에서 가로, 세로, 또는 대각선(양방향) 을 포함하여, 최소 2개 이상의 줄에서 모든 숫자가 *로 대체되면 빙고가 성립 된다.
# 6. 2개 이상의 빙고 줄이 완성되면 사용자가 승리.

# 코드 작성
import random

# 1. 사용자로부터 보드 사이즈 N값 입력 받기. 유효하지 않은 사이즈라면 다시 입력받기
while True :
    board_size = int(input("빙고판의 사이즈를 입력하세요. (3~6 사이의 수) : "))
    
    if 3 <= board_size <= 6 :
        break
    else :
        print("3부터 6사이의 정수를 입력하세요. ")
        
# 2. 빙고 보드생성 N x N 크기의 난수로 채워진 1차원 리스트 생성 (2차원 리스트가 아닌 1차원으로 N x N 사이즈를 생성..?)
board = []

# 랜덤으로 나온 숫자가 중복되는지 확인하기 위한 0이 36개 채워진 리스트
check = [0] * (36)

# 2-1. 중복 출력 후 검증과정 거쳐야됨.. 일일히 반복? 너무 비효율적. 36번 X 36번 돌아야됨 sample? 사용불가. 
while len(board) < (board_size * board_size) : 
    rand_value = random.randint(1,36)
    
    if check[rand_value-1] == 0 :
        check[rand_value-1] = 1
        board.append(rand_value) 
    
# 3. 보드판 출력하는 코드 작성
count = 1
while True : 
    bingo = 0
    rand_answer = random.randint(1,36)
    input("랜덤 정수를 뽑으려면 엔터키를 클릭하세요.")
    print(f"Random Number {count} : {rand_answer}")
    
    
    for i in range(len(board)) :
        if board[i] == rand_answer :
            board[i] = "*"
    
    # 보드판 출력 코드
    x = 1
    for value in board :
        if x % board_size == 0 :
            print(value)
        else :
            print(value, end=" ")
        x += 1
    
    # 가로 빙고 확인
    rows = board_size
    rows2 = 0
    
    for _ in range(board_size) :
        star = 0
        
        for i in board[rows2:rows] :
            if i == "*" :
                star += 1
        
        if star == board_size :
            bingo += 1
            
        rows += board_size
        rows2 += board_size
    
    # 세로 빙고 확인
    for i in range(board_size) :
        star = 0
        
        for i in board[i::board_size] :
            if i == "*" :
                star += 1
        
        if star == board_size :
            bingo += 1
    
    # 대각선 빙고 확인
    # 왼쪽 대각선 빙고
    star = 0
    for i in board[::board_size+1] :
        
        if i == "*" :
            star += 1
        
        if star == board_size :
            bingo += 1
    
    # 오른 대각선 빙고
    star = 0
    board_ver2 = board[board_size-1::board_size-1]
    del board_ver2[-1]
    
    for i in board_ver2 :
        if i == "*" :
            star += 1
        
        if star == board_size :
            bingo += 1
    
    if bingo >= 2 :
        print("2 빙고 이상을 완성했습니다. 게임을 종료합니다. ")
        print(bingo)
        break
    
    count += 1