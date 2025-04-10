# 알고리즘 작성
# 1. 빈 리스트 생성
# 2. 사용자가 도서 제목을 입력하면 해당 제목을 도서 목록에 추가하는 기능
# 3. 사용자가 종료라고 입력할 때까지 프로세스 반복
# 4. 마지막에 전체 도서 목록 출력

books = []

while True :
    title = input("도서 제목을 입력하세요 (종료하려면 '종료' 입력) : ")
    
    if title == '종료' :
        break
    books.append(title)
    
print("도서 목록 :",books)