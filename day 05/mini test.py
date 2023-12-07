#양의 정수를 입력 받아 시 분 초 형태로 출력하는 프로그램
#1.양의 정수를 입력받기
#2.양의 정수를 시 분 초 형태로 나타내기

#user = int(input("양의 정수를 입력해주세요 : "))
#min = user // 60
#sec = user - min*60
#hour = user // 3600

#print(f"{hour}:{min}:{sec}")


#뉴스 기사 단어 별로 정렬화 퀴즈
#1.뉴스 기사 스크랩 : 웹에서 아무 뉴스 기사를 선택하여 그 내용을 문자열로 복사합니다.
#2.문자열 분리 및 리스트 화 : 스크랩한 뉴스 기사 제목을 개별적으로 분리하여 리스트에 저장합니다.
#여기서 파이썬의 문자열 함수를 활용하여 제목들을 적절히 분리하고 처리하는 방법을 고민해보세요
#3.리스트 정렬 : 저장한 뉴스 기사 알파벳 순서대로 정렬합니다. 이때 파이썬 리스트 정렬기능을 사용하여 정렬을 수행하세요
#4결과 출력 : 정렬된 리스트들을 출력하여 최종적으로 알파벳 순으로 정렬된 뉴스 기사를 확인할 수 있게 합니다.


#점메추 프로그램
#1.리스트 생성 : 메인 음식, 후식, 음료 각각에 대한 이모지 리스트를 생성합니다. 각 리스트는 최소 5개 이상의 음식으로 구성해야합니다.
#2.랜덤 추천 기능 구현 : 프로그램 사용자가 실행을 하면 , 각 카테고리[메인음식, 후식, 음료]에서 랜덤으로 하나씩 음식을 선택하여
# 조합을 만들고 이를 출력합니다.
#이때 파이썬의 random모듈을 활용합니다.
#3.출력 포맷 : 선택 된 이모지 조합을 메인 음식:[제육] 후식:[탕후루] 음료:[아아]형식으로 출력
import random

main_food = ['🍱','🍖','🍚','🍝','🥖']
dessert=['🍦','🍬','🍩','🍫','🍿']
drink=['☕','🥛','🍷','🍸','🍺']

user1=input(main_food)
choose = random.choice(main_food)
print(choose)
user2=input(dessert)
choose2=random.choice(dessert)
print(choose2)
user3=input(drink)
choose3=random.choice(drink)
print(choose3)

list_result = [choose, choose2, choose3]
print(list_result)

print(f"메인음식:[{choose}] 후식:[{choose2}] 음료:[{choose3}]")


