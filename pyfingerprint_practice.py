from pyfingerprint.pyfingerprint import PyFingerprint

try:
    # 포트: 실제 연결된 포트로 바꿔야 함 (예: /dev/ttyS0 또는 /dev/serial0 또는 /dev/ttyUSB0)
    f = PyFingerprint('/dev/ttyS0', 57600, 0xFFFFFFFF, 0x00000000)

except Exception as e:
    print('❌ 지문 인식기 연결 실패!')
    print('오류 내용:', str(e))
    exit(1)

print('✅ 지문 인식기 연결 성공!')
print('등록된 지문 수:', f.getTemplateCount())

print('지문을 스캔해주세요...')

# 손가락이 올라올 때까지 기다림
while f.readImage() == False:
    pass

# 이미지 → 특성 데이터로 변환
f.convertImage(0x01)

# DB와 비교
result = f.searchTemplate()
positionNumber = result[0]
accuracyScore = result[1]

if positionNumber == -1:
    print('일치하는 지문 없음')
else:
    print(f'지문 일치! 위치: {positionNumber}, 정확도: {accuracyScore}')