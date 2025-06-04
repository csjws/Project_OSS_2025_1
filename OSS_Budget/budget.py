import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    # 날짜도 입력받도록 수정
    def add_expense(self, date, category, description, amount):
        expense = Expense(date, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")
        

    #선택한 두 개의 (년도, 월) 지출을 비교
    def compare_monthly_expenses(self, year1, month1, year2, month2):

        expenses1 = [e for e in self.expenses
                  if e.date.startswith(f"{year1}-{str(month1).zfill(2)}")]
        total1 = sum(e.amount for e in expenses1)

        expenses2 = [e for e in self.expenses
                  if e.date.startswith(f"{year2}-{str(month2).zfill(2)}")]
        total2 = sum(e.amount for e in expenses2)

        print(f"\n{year1}년 {month1}월 총 지출: {total1}원")
        print(f"{year2}년 {month2}월 총 지출: {total2}원")

        diff = total1 - total2
        if diff > 0:
            print(f"{year2}년 {month2}월보다 {year1}년 {month1}월이 {diff}원 더 많이 썼습니다.\n")
        elif diff < 0:
            print(f"{year1}년 {month1}월보다 {year2}년 {month2}월이 {abs(diff)}원 더 많이 썼습니다.\n")
        else:
            print("두 달의 지출이 동일합니다.\n")
