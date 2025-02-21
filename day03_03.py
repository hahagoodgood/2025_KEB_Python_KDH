# Assignment
# v2.3) 다음 코드에서 딕셔너리를 제거하고 리스트만 사용하여 동일하게 동작하도록 코드를 수정하시오.
import random
drinks = ["위스키", "와인", "소주", "고량주"]
snacks = ["초콜릿", "치즈", "삽겹살", "양꼬치"]

drinks.append("사케")
snacks.append("광어회")
snacks[0] = "낙곱새"

def print_matched_snack(drinks, snacks) -> int:
    print("다음 술중에 고르세요.")
    for i in range(len(drinks)):
        print(f"{i+1}) {drinks[i]}", end="  ")
    num = int(input(f'{len(drinks)+1}) 아무거나  {len(drinks)+2}) 종료 : '))
    if num < 0 or num > len(drinks)+2:
        return -1
    elif num == len(drinks)+2:
        print('다음에 또 오세요')
        return 0
    elif num == len(drinks)+1:
        num = random.randint(1, len(drinks))
    print(f'{drinks[num-1]}에 어울리는 안주는 {snacks[num-1]} 입니다')
    return 1


while True:
    # menu = input(f'다음 술중에 고르세요.\n1) {drinks[0]}   2) {drinks[1]}   3) {drinks[2]}   4) {drinks[3]}   5) {drinks[4]}   6) 아무거나   7) 종료 : ')
    # if menu == '1':
    #     print(f'{drinks[0]}에 어울리는 안주는 {snacks[0]} 입니다')
    # elif menu == '2':
    #     print(f'{drinks[1]}에 어울리는 안주는 {snacks[1]} 입니다')
    # elif menu == '3':
    #     print(f'{drinks[2]}에 어울리는 안주는 {snacks[2]} 입니다')
    # elif menu == '4':
    #     print(f'{drinks[3]}에 어울리는 안주는 {snacks[3]} 입니다')
    # elif menu == '5':
    #     print(f'{drinks[4]}에 어울리는 안주는 {snacks[4]} 입니다')
    # elif menu == '6':
    #     random_index = random.randint(0, len(drinks)-1)
    #     print(f'{drinks[random_index]}에 어울리는 안주는 {snacks[random_index]} 입니다')
    # elif menu == '7':
    #     print(f'다음에 또 오세요')
    #     break
    i = print_matched_snack(drinks, snacks)
    if i == 0:
        break