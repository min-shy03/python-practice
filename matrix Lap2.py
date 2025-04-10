rows = int(input("행의 수를 입력하세요 : ")) # 리스트 내 리스트 의 개수
cols = int(input("열의 수를 입력하세요 : ")) # 행 내의 요소 개수 (가장 안 쪽)

matrix = [[0 for _ in range(cols)] for _ in range(rows)] # 가짜 숫자로 채워 진 리스트 생성 -> 사용자에게 입력 받을 예정

for i in range(rows) :
    for item in range(cols) :
        matrix[i][item] = int(input(f"[{i}][{item}]에 넣을 값 입력 : "))

for i in matrix :
    for item in i :
        print(item, end=" ")
    
    print("")