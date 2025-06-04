from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 두 달의 지출 비교")
        print("5. 종료")
        choice = input("선택 > ")

        if choice == "1":
            date = input("날짜입력(예: 2024-06-04): ")
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(date, category, description, amount)

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()
        
        elif choice == "4":
            try:
                year1 = int(input("첫 번째 년도(ex : 2025): "))
                month1 = int(input("첫 번째 월(ex : 1): "))
                year2 = int(input("두 번째 년도(ex : 2025): "))
                month2 = int(input("두 번째 월(ex : 1): "))
            except ValueError:
                print("잘못된 입력입니다.\n")
                continue
            budget.compare_monthly_expenses(year1, month1, year2, month2)

        elif choice == "5":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()