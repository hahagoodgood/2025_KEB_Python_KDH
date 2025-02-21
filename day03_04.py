# Assignment
# v2.5) while 안쪽의 하드코딩된 코드를 함수화하시오.
import random

drinks = ["위스키", "와인", "소주", "고량주"]
snacks = ["초콜릿", "치즈", "삽겹살", "양꼬치"]

drinks.append("사케")
snacks.append("광어회")
snacks[0] = "낙곱새"
drinks.append("데킬라")
snacks.append("소금")

def print_menu(n):
    print(f'{drinks[n]}에 어울리는 안주는 {snacks[n]} 입니다')


menu_list = '다음 술중에 고르세요.\n'
for i in range(len(drinks)):
    menu_list = menu_list + f'{i+1}) {drinks[i]}  '
menu_list = menu_list + f'{len(drinks)+1}) 아무거나  {len(drinks)+2}) 종료 : '

while True:
    menu = int(input(menu_list))
    if menu >= 1 and menu <= len(drinks)+2:
        if menu in range(1,len(drinks)+2):
            if menu == len(drinks)+1:
                menu = random.randint(0, len(drinks) - 1)
            print_menu(int(menu) - 1)
        else :
            print(f'다음에 또 오세요')
            break
