# Assignment
# v2.3) 다음 코드에서 딕셔너리를 제거하고 리스트만 사용하여 동일하게 동작하도록 코드를 수정하시오.
import random
# drinks_foods = {"위스키": "초콜릿", "와인": "치즈", "소주": "삽겹살", "고량주": "양꼬치"}
# japan_drinks_foods = {"사케": "광어회", "위스키": "낙곱새"}
# drinks_foods.update(japan_drinks_foods)
# drinks = list(drinks_foods)
drinks = ["위스키", "와인", "소주", "고량주"]
foods = ["초콜릿", "치츠", "삼겹살", "양꼬치"]
drinks.append("사케")
foods.append("광어회")
foods[0] = "낙곱새"

while True:
    menu = input(f'다음 술중에 고르세요.\n1) {drinks[0]}   2) {drinks[1]}   3) {drinks[2]}   4) {drinks[3]}   5) {drinks[4]}   6) 아무거나   7) 종료 : ')
    if menu == '1':
        print(f'{drinks[0]}에 어울리는 안주는 {foods[0]} 입니다')
    elif menu == '2':
        print(f'{drinks[1]}에 어울리는 안주는 {foods[1]} 입니다')
    elif menu == '3':
        print(f'{drinks[2]}에 어울리는 안주는 {foods[2]} 입니다')
    elif menu == '4':
        print(f'{drinks[3]}에 어울리는 안주는 {foods[3]} 입니다')
    elif menu == '5':
        print(f'{drinks[4]}에 어울리는 안주는 {foods[4]} 입니다')
    elif menu == '6':
        random_drink = random.randint(0, len(drinks) - 1)
        print(f'{drinks[random_drink]}에 어울리는 안주는 {foods[random_drink]} 입니다')
    elif menu == '7':
        print(f'다음에 또 오세요')
        break