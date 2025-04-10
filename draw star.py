# 자연수 N을 입력 받아 지정된 패턴으로 * 출력한다.

# 첫 번째 줄부터 N번째 줄까지 별의 개수를 1씩 증가시킨다.
# N번째 줄 이후부터는 별의 개수를 감소시켜 마지막 줄에는 별 1개를 출력한다.

# 코드 작성
# 1. 사용자에게 자연수 입력받기
value = int(input("자연수 N 입력 : "))

# 2. N번째 줄까지 패턴
for i in range(1,value+1) :
    print("*" * i)

# 3. N번째 줄 이후 패턴
for i in range(value-1, 0, -1) :
    print("*" * i)