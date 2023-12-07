#마무리 퀴즈
#1. 영어점수, 등급 매기기
#0부터 100사이의 영어점수를 입력해보세요 점수에 따라 ABCD등급을 매겨드릴게요
#나머지는 아쉽게도 탈락이에요라고 알려드려요

#score = int(input("영어점수를 입력하시오:"))
#if score >=90 :
   # print("A")
#elif score >=80 :
  #  print("B")
#elif score >=70 :
   # print("C")
#elif score >=60 :
  #  print("D")
#else :
  #  print("아쉽게도 탈락이에요!")

#2.각도의 비밀을 밝혀라
#각도를 입력해주세요 예각이면 1 직각이면2 둔각이면3 평각이면4로 분류해서 알려드릴게요

#angle = int(input("각도를 입력해주세요: "))

#if angle<90 :
   # print("예각")
#elif angle == 90 :
   # print("직각")
#elif angle ==180 :
   # print("평각")
#else :
    #print("둔각")


#3대소문자 바꾸기
#문자열을 입력하면 대문자는 소문자로 소문자는 대문자로 바꿔드릴게요

#user = input("문자열을 입력해주세요: ")

#if user.isupper():
    #print(user.lower())
#elif user.islower():
    #print(user.upper())
#else:
    #print("끝!")



#4.점수에 따른 등급과 피드백
#국 영 수 점수를 입력해주세요 평균 점수에 따라 ABC등급을 매겨드리고 만약 한 과목이 100점이면 굿 60점이하면 배드라고 알려드릴게요
sc1 = int(input("국어점수를 입력하시오:"))
sc2 = int(input("영어점수를 입력하시오:"))
sc3 = int(input("수학점수를 입력하시오:"))

total = (sc1+sc2+sc3)/3


if total >90:
    print("A")
    if sc1 or sc2 or sc3 == 100:
        print("GOOD!")
elif total >80:
    print("B")
    if sc1 or sc2 or sc3 == 100:
        print("GOOD!")
elif total >70:
    print("C")
    if sc1 or sc2 or sc3 == 100:
        print("GOOD!")
else:
    print("탈락입니다")


100
