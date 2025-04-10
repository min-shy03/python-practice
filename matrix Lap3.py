# 학생 성적 관리 프로그램 작성

import time

# 학생 목록 담을 리스트 생성
student_list = []
student_total_avg = 0.0
total_avg = 0.0

# 프로그램을 시작할 시점의 시간 저장
start_time = time.time()

def line() :
    print("===============================")
# 학생 이름, 성적, 학번 등을 담을 리스트 생성 후 학생 목록 리스트에 담기
while True :
    line()
    print("<학생 성적 관리 프로그램>")
    print("1. 학생 성적 입력")
    print("2. 학생 목록 출력")
    print("3. 프로그램 종료\n")
    print(f"현재 입력 된 학생 수 : {len(student_list)}명")
    print(f"전체 학생 평균 값 : {student_total_avg}")
    line()
    
    user_want = input("원하는 메뉴를 선택하세요 : ")
    
    # 1번 선택 시 학생 정보 추가 
    if user_want == "1" :
        line()
        while True :
            student_num = input("학번을 입력하세요 : ")
            
            if student_num.isdigit() :
                student_num = int(student_num)
                break
            else :
                print("학번이 올바르게 입력되지 않았습니다 다시 입력하세요.")
                
                
        while True : 
            student_name = input("이름을 입력하세요 : ")
    
            if not student_name.isalpha() :
                print("이름이 올바르게 입력되지 않았습니다 다시 입력하세요.")
            else : 
                break
            
        while True :
            korean = input("국어 성적을 입력하세요 : ")
                
            if korean.isdigit() and 0 <= int(korean) <= 100 :
                korean = int(korean)
                break
            else :
                print("국어 성적이 올바르게 입력되지 않았습니다 다시 입력하세요.")
                    
            
        while True :
            eng = input("영어 성적을 입력하세요 : ")
            
            if eng.isdigit() and 0 <= int(eng) <= 100 :
                eng = int(eng)
                break
            else :
                print("영어 성적이 올바르게 입력되지 않았습니다 다시 입력하세요.")
                    
        while True :
            math = input("수학 성적을 입력하세요 : ")
            
            if math.isdigit() and 0 <= int(math) <= 100:
                math = int(math)
                break
            else :
                print("수학 성적이 올바르게 입력되지 않았습니다 다시 입력하세요.")
                
            
        total = korean + eng + math
        
        avg = round((total / 3) , 2)
        
        student_list.append([student_num,student_name, korean, eng, math, total, avg])
        
        total_avg += avg 
        
        student_total_avg = round(total_avg / len(student_list), 2)
            
    
    # 2번 선택 시 학생 목록 출력
    elif user_want == "2" :
        while True :
            line()
            print("<학생 목록 출력>")
            print("1. 학생 개인 목록 출력")
            print("2. 학생 전체 목록 출력")
            print("3. 뒤로 가기\n")
            print(f"현재 입력 된 학생 수 : {len(student_list)}명")
            line()
            user_want_in_menu2 = input("원하는 메뉴를 선택하세요 : ")
            
            
            if user_want_in_menu2 == "1" :
                line()
                print("<현재 입력된 학생 목록>\n")
                count = 1
                for student in student_list :
                    print(f"{count}. {student[1]}")
                    count += 1
                line()     
                
                while True :
                    user_choose_stu = (input("성적을 가져올 학생의 번호를 입력하세요 : "))
                
                    if user_choose_stu.isdigit() and 1 <= int(user_choose_stu) <= len(student_list) + 1 :
                        user_choose_stu = int(user_choose_stu) - 1
                        break
                    else :
                        print("학생 번호가 올바르지 않습니다. 다시 입력하세요.")
                
                line()
                print(f"id : {student_list[user_choose_stu][0]} ㅣ "
                      f"name : {student_list[user_choose_stu][1]} ㅣ "
                      f"kor : {student_list[user_choose_stu][2]} ㅣ "
                      f"eng : {student_list[user_choose_stu][3]} ㅣ "
                      f"math : {student_list[user_choose_stu][4]} ㅣ "
                      f"sum : {student_list[user_choose_stu][5]} ㅣ "
                      f"avg : {student_list[user_choose_stu][6]}"
                      )
            
            elif user_want_in_menu2 == "2" :
                line()
                for i in range(len(student_list)) :
                    print(f"id : {student_list[i][0]} ㅣ "
                      f"name : {student_list[i][1]} ㅣ "
                      f"kor : {student_list[i][2]} ㅣ "
                      f"eng : {student_list[i][3]} ㅣ "
                      f"math : {student_list[i][4]} ㅣ "
                      f"sum : {student_list[i][5]} ㅣ "
                      f"avg : {student_list[i][6]}"
                      )
                    
            elif user_want_in_menu2 == "3" :
                break
            else :
                print("메뉴에 존재하지 않는 번호입니다. 다시 입력하세요")
        
    # 3번 선택 시 프로그램 종료
    elif user_want == "3" :
        line()
        print("프로그램을 종료합니다")
        break
    else :
        print("메뉴에 존재하지 않는 번호입니다. 다시 입력하세요")

#프로그램이 끝난 시점의 시간 저장
end_time = time.time()

# 프로그램이 실행되고 종료될 때까지 걸린 시간 계산
print(f"걸린 시간 : {end_time - start_time :.2f}초")