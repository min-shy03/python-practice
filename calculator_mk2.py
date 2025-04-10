# 괄호 부터 처리

def calculator(iv) :
    operand_list = []
    operator_list = []
    
    operand = ""
    operator = ""
    
    count = 0
    
    # 챗지피티 ㅅㅂ롬이 답을 스포함.. 괄호 쌍 구분 -> 왜 이걸 생각을 못했을까??
    while '(' in iv:
        # 가장 안쪽 괄호쌍 찾기
        for i, ch in enumerate(iv):
            if ch == '(':
                start = i
            elif ch == ')':
                end = i
                break
        
        # 괄호 안만 계산
        result = calculator(iv[start+1:end])
        iv = iv[:start] + str(result) + iv[end+1:]
    
    # 연산자와 피연산자 구분하기
    for bar in iv :
        # 가장 마지막에 오는 피연산자 담기 위한 카운트 변수
        count += 1
        # 피연산자일 경우
        if bar.isdigit() :
            operand += bar
            # 연산자를 리스트에 담기
            if operator != "" : 
                operator_list.append(operator)
            # 현재 연산자 초기화
            operator = ""
            
        # 연산자일 경우 변수에 연산자 담기
        if not bar.isdigit() or count == len(iv) :
            operator += bar
            # 피연산자 리스트에 담기
            if operand != "" :
                operand_list.append(int(operand))
            # 현재 피연산자 초기화
            operand = "" 
    
    # 연산자의 우선순위 리스트로 표현하기
    priority_operator = [["**"],["*","/","%","//"],["+","-"]]                

    for ops in priority_operator :
        # 리스트 인덱스를 불러올 카운트 변수
        count = 0 
        
        # 제곱 일 때 우측 연산부터 실행
        if "**" in operator_list :
            count = len(operator_list) - 1  # 마지막 연산자부터 시작
            while count >= 0:
                if operator_list[count] == '**':
                    operand_list[count] = operand_list[count] ** operand_list[count+1]
                    del operand_list[count+1]
                    del operator_list[count]
                count -= 1
        # 제곱이 아닐 경우 원래대로 좌측 연산부터 실행
        else :
            while count < len(operator_list) :
                if operator_list[count] in ops :
                    o = operator_list[count]
                    if o == "*" :
                        operand_list[count] = operand_list[count] * operand_list[count+1]
                        del operand_list[count+1]
                        del operator_list[count]
                        count = 0
                        continue
                    elif o == "/" :
                        operand_list[count] = operand_list[count] / operand_list[count+1]
                        del operand_list[count+1]
                        del operator_list[count]
                        count = 0
                        continue
                    elif o == "//" :
                        operand_list[count] = operand_list[count] // operand_list[count+1]
                        del operand_list[count+1]
                        del operator_list[count]
                        count = 0
                        continue
                    elif o == "%" :
                        operand_list[count] = operand_list[count] % operand_list[count+1]
                        del operand_list[count+1]
                        del operator_list[count]
                        count = 0
                        continue
                    elif o == "+" :
                        operand_list[count] = operand_list[count] + operand_list[count+1]
                        del operand_list[count+1]
                        del operator_list[count]
                        count = 0
                        continue
                    elif o == "-" :
                        operand_list[count] = operand_list[count] - operand_list[count+1]
                        del operand_list[count+1]
                        del operator_list[count]
                        count = 0
                        continue
                    
                count += 1
    
    # 수식 계산 후 최종 결과 반환
    return operand_list[0]


print(calculator(input())) 