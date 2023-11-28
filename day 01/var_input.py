#input은 콘솔에 유저가 입력한 값을 받는 함수
name = input("당신의 이름은 무엇입니까?")
age = input("당신의 나이는 몇살입니까?")
first = input("외향입니까? 내향입니까? (E 또는 I 입력)")
second = input("직관입니까? 감각적입니까? (N 또는 S 입력)")
third = input("감정적입니까? 현실적입니까? (F 또는 T 입력)")
fourth = input("계획적입니까? 즉흥적입니까? (J 또는 P 입력)")

print(f"{name}님의 나이는 {age}이고 mbti는 {first}{second}{third}{fourth}입니다.")


