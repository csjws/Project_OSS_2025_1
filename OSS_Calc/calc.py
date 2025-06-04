import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x500")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['='],
            ['C→F', 'F→C']  # 변환 버튼 추가
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
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        elif char == 'C→F':
            self.convert_c_to_f()
        elif char == 'F→C':
            self.convert_f_to_c()
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    #섭씨 -> 화씨
    def convert_c_to_f(self):
        try:
            celsius = float(self.expression)
            fahrenheit = (celsius * 9/5) + 32
            self.expression = str(round(fahrenheit, 2))  
        except Exception:
            self.expression = "에러"

    #화시 -> 섭씨
    def convert_f_to_c(self):
        try:
            fahrenheit = float(self.expression)
            celsius = (fahrenheit - 32) * 5/9
            self.expression = str(round(celsius, 2))
        except Exception:
            self.expression = "에러"