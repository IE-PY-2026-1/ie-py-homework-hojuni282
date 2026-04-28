# [2차 과제] 스마트 소비 습관 분석 및 지출 관리 시스템 V1.0
print("=== 대학생 스마트 소비 습관 분석 시스템 ===")

# 1. 데이터 입력 및 형변환
food = int(input("1. 오늘 사용한 식비(원): "))
cafe = int(input("2. 오늘 사용한 카페비(원): "))
shopping = int(input("3. 오늘 사용한 쇼핑비(원): "))
transport = int(input("4. 오늘 사용한 교통비(원): "))

# 2. 리스트 구조 활용
expenses = [food, cafe, shopping, transport]

# 3. 산술 연산 및 총액 계산
total_sum = sum(expenses)

print("-" * 30)
print(f"오늘의 총 지출액: {total_sum}원")

# 4. 카테고리별 소비 비율 출력
print("\n[카테고리별 지출 비율]")
if total_sum > 0:
    categories = ["식비", "카페", "쇼핑", "교통"]
    for i in range(len(expenses)):
        ratio = (expenses[i] / total_sum) * 100
        print(f"- {categories[i]}: {ratio:.1f}%")
else:
    print("지출 내역이 없습니다.")

# 5. 소비 유형 분석 (if-elif-else)
if total_sum >= 50000:
    grade = "과소비형 (C)"
elif total_sum >= 20000:
    grade = "균형형 (B)"
else:
    grade = "절약형 (A)"

# 6. 논리 연산자 활용 및 최종 출력
print(f"당신의 소비 등급: {grade}")
if (cafe > total_sum * 0.5) or (shopping >= 30000):
    print("⚠️ [특별 경고] 특정 항목(카페/쇼핑) 지출이 매우 높습니다!")

print("-" * 30)
print("프로그램을 종료합니다.")
