# 차량이 어떤 거리를 이동하는 데 걸린 시간과 이동 거리를 바탕으로 평균 속도 계산 프로그램 작성

# 알고리즘 작성
# 1. 사용자로부터 출발 시간과 도착 시간(시, 분 별도 입력), 이동 거리 입력받기

# 2. 차량의 평균 속도를 km/h 단위로 계산하고, 그 속도가 "느림", "보통", "빠름" 중 어느 것에 해당하는지 출력

# 3. 소요 시간 공식 (도착 시간 * 60 + 도착 분) - (출발 시간 * 60 + 출발 분)

# 4. 출발 시간의 물리적 시간이 도착 시간보다 클 경우 ex) 23시 출발 1시 도착
# ((도착 시간 * 60 + 도착 분) + 1440) - (출발 시간 * 60 + 출발 분)

# 5. 평균 속도 계산 = 거리 / 시간 / 60 (3에서 구한 총 소요 시간은 분 단위임으로 60으로 나누기.)

# 6. 총 소요 시간은 60으로 나눈 후 나머지와 몫을 구해 ??시 ??분의 형태로 출력 ex) 120분 소요 = 2시간 0분 소요요


# 코드 작성
while True :
    # 사용자로부터 출발 시간(시), 출발 시간(분), 도착 시간(시), 도착 시간(분), 이동 거리(km) 입력받기
    while True :
        while True : 
            start_time_hour = int(input("출발 시간 입력 ??시 ??분 (0~23시) : "))
            # 0시부터 23시까지 입력 받기 24시 == 0시 임으로 24도 오류로 처리
            if 0 <= start_time_hour < 24 :
                break
            else :
                print("다시 입력")
        
        while True :
            # 0분 부터 59분까지 입력 받기 60분 == 다음 시각임으로 60분도 오류 처리
            start_time_minute = int(input(f"출발 분 입력 {start_time_hour}시 ??분 (0~59): "))
            
            if 0 <= start_time_minute < 60 :
                break
            else :
                print("다시 입력")
        
        while True : 
            arrival_time_hour = int(input("도착 시간 입력 ??시 ??분 (0~23시) : "))
            # 0시부터 23시까지 입력 받기 24시 == 0시 임으로 24도 오류로 처리
            if 0 <= arrival_time_hour < 24 :
                break
            else :
                print("다시 입력")
        
        while True :
            # 0분 부터 59분까지 입력 받기 60분 == 다음 시각임으로 60분도 오류 처리
            arrival_time_minute = int(input(f"도착 분 입력 {arrival_time_hour}시 ??분 (0~59): "))
            
            if 0 <= arrival_time_minute < 60 :
                break
            else :
                print("다시 입력")
        
        total_start_time = (start_time_hour * 60) + start_time_minute
        total_arrival_time = (arrival_time_hour * 60) + arrival_time_minute
        
        # 출발 시간 == 도착 시간이면 날짜를 늘려야 하지만 그것까진 아직 구현이 안되므로 오류로 출력
        if total_start_time == total_arrival_time :
            print("다시 입력")
        else :
            break 
    
    # 총 소요 시간 계산
    
    # 출발 시간의 물리적 시간이 도착 시간보다 작을 경우
    if total_start_time <= total_arrival_time :
        total_time = total_arrival_time - total_start_time
    # 출발 시간의 물리적 시간이 도착 시간보다 클 경우
    else :
        total_time = (total_arrival_time + 1440) - total_start_time
    
    # 총 소요 시간을 60으로 나눈 후 나머지와 몫을 구해 ??시 ??분의 형태로 출력
    total_time_hour, total_time_minute = divmod(total_time, 60)
    
    # 이동 거리 입력 받기
    while True :
        distance = float(input("이동 거리 입력(km) : "))
        if distance <= 0 :
            print("다시 입력")
        else :
            break
    
    # 평균 속도 계산 거리 / 시간 / 60
    speed_avg = distance / (total_time / 60)
    
    # 속도가 어느 정도인지 계산
    speed_status = ""
    if speed_avg < 60 :
        speed_status = "느림"
    elif speed_avg < 90 :
        speed_status = "보통"
    else :
        speed_status = "빠름"
    
    # 출력
    print("============================================")
    print(f"이동 거리 : {distance}km")
    print(f"출발 시간 : {start_time_hour}시 {start_time_minute}분")
    print(f"도착 시간 : {arrival_time_hour}시 {arrival_time_minute}분")
    print(f"총 소요 시간 : {total_time_hour}시간 {total_time_minute}분")
    print(f"평균 속도 : {speed_avg}km/h")
    print(f"속도 상태 : {speed_status}")
    print("============================================")
    break