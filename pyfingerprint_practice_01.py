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