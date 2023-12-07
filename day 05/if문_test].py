# 1.양의 홀수? 양의 짝수 ? 음의 홀수인지, 음의 짝수인지, 아니면 0인지 확인해보기

# user = int(input("숫자를 입력하시오: "))

# if user>0 and user%2==0:
#   print("양의 짝수")
# elif user<0 and user%2==0:
#   print("음의 짝수")
# elif user>0 and user%2==1:
#   print("양의 홀수")
# elif user == 0 :
#   print("0")
# else :
#   print("음의 홀수")

# 중첩 사용해서

# if user > 0:
# if user %2==0:
# print("양의 짝수 입니다.")
# else :
#  print("양의 홀수 입니다.")
#  elif user < 0 :
#   if user %2==0:
# print("음의 짝수 입니다.")
#  else:
# print("음의 홀수 입니다.")
# else:
# print("0입니다")


# 2. 알파벳 탐지기
# 안녕하세요, 문자 한개를 입력해주세요! 만약 알파벳이라면 알파벳입니다를, 그렇지 않다면 알파벳이 아니에요 라고 알려드릴게요!
#파이썬 특성상 한글도 알파벳으로 인식
#text = input("글자를 입력하세요: ")
#if text.isalpha():
    #print("알파벳입니다.")
#else:
   # print("알파벳이 아니에요!")

    # 비밀번호 유효 타입체크
    # 비밀번호를 입력을 받고
    # 비밀번호의 시작이 영어 알파벳 대문자로 시작하면 [A,E]
    # 비밀번호를 옳게 설정했습니다
    # 비밀번호 첫글자는 대문자로 설정해주세요!

user = input("비밀번호를 입력하세요:")
if not (user[0].isupper()):
        print("비밀번호의 첫글자는 대문자로 설정해주세요!")
elif len(user) < 8 :
    print("비밀번호를 8글자 이상으로 해주세요!")
elif user.isalpha():
    print("비밀번호에 특수문자를 넣어주세요")
else:
    print("잘 설정하셨습니다.")








