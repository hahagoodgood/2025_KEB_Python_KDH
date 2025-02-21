# Assignment
# v2.3) 다음 코드에서 딕셔너리를 제거하고 리스트만 사용하여 동일하게 동작하도록 코드를 수정하시오.
import random
drinks = ["위스키", "와인", "소주", "고량주"]
snacks = ["초콜릿", "치즈", "삽겹살", "양꼬치"]

drinks.append("사케")
snacks.append("광어회")
snacks[0] = "낙곱새"

while True:
    print("다음 술중에 고르세요.")
    for i in range(len(drinks)):
        print(f"{i + 1}) {drinks[i]}", end="  ")
    num = int(input(f'{len(drinks) + 1}) 아무거나  {len(drinks) + 2}) 종료 : '))
    if num == len(drinks) + 2:
        print('다음에 또 오세요')
        break
    elif num == len(drinks) + 1:
        num = random.randint(1, len(drinks))

    if num >= 1 and num <= len(drinks):
        print(f'{drinks[num - 1]}에 어울리는 안주는 {snacks[num - 1]} 입니다')
