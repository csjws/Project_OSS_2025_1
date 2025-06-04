import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x450")

        self.expression = ""
        self.last_result = ""  # 가장 최근 계산 결과 저장

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=', 'COPY']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
            self.entry.delete(0, tk.END)
        elif char == '=':
            try:
                result = str(eval(self.expression))
                full_expression = f"{self.expression}={result}"
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, full_expression)

                self.last_result = result      # 결과 저장
                self.expression = result       # 다음 입력부터 결과값으로 시작
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "에러")
                self.expression = ""
                self.last_result = ""
        elif char == 'COPY':
            # entry 내용 전체를 클립보드에 복사
            self.root.clipboard_clear()
            self.root.clipboard_append(self.entry.get())
            print("전체 수식이 복사되었습니다.")
        else:
            # 수식이 "5+1=6" 형태일 때, 새로 시작하도록 처리
            if '=' in self.entry.get():
                self.expression = self.last_result

            self.expression += str(char)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)
