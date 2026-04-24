import tkinter as tk
from tkinter import ttk, messagebox
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title('Advanced Scientific Calculator')
        self.root.geometry('520x700')
        self.root.configure(bg='#1e1e1e')
        self.expr = tk.StringVar()
        self.memory = 0
        self._build_ui()

    def _build_ui(self):
        entry = tk.Entry(self.root, textvariable=self.expr, font=('Segoe UI', 24), bd=8,
                         relief='flat', justify='right', bg='white')
        entry.pack(fill='x', padx=10, pady=10, ipady=12)

        frame = tk.Frame(self.root, bg='#1e1e1e')
        frame.pack(expand=True, fill='both', padx=10, pady=10)

        buttons = [
            ['MC','MR','M+','M-','C'],
            ['(',')','√','x²','⌫'],
            ['7','8','9','/','sin'],
            ['4','5','6','*','cos'],
            ['1','2','3','-','tan'],
            ['0','.','π','+','log'],
            ['e','^','!','1/x','=']
        ]

        for r,row in enumerate(buttons):
            for c,text in enumerate(row):
                btn = tk.Button(frame, text=text, font=('Segoe UI',16), bd=0,
                                command=lambda t=text:self.click(t),
                                bg='#2d2d30', fg='white', activebackground='#3e3e42')
                btn.grid(row=r, column=c, sticky='nsew', padx=2, pady=2, ipadx=8, ipady=16)
        for i in range(len(buttons)):
            frame.rowconfigure(i, weight=1)
        for i in range(5):
            frame.columnconfigure(i, weight=1)

    def click(self, key):
        try:
            if key == '=':
                self.calculate()
            elif key == 'C':
                self.expr.set('')
            elif key == '⌫':
                self.expr.set(self.expr.get()[:-1])
            elif key == 'π':
                self.expr.set(self.expr.get() + 'pi')
            elif key == 'e':
                self.expr.set(self.expr.get() + 'e')
            elif key == '^':
                self.expr.set(self.expr.get() + '**')
            elif key == '√':
                self.expr.set(self.expr.get() + 'sqrt(')
            elif key == 'x²':
                self.expr.set(self.expr.get() + '**2')
            elif key == '1/x':
                self.expr.set('1/(' + self.expr.get() + ')')
            elif key in ['sin','cos','tan','log']:
                self.expr.set(self.expr.get() + key + '(')
            elif key == '!':
                val = int(eval(self.expr.get(), self.safe_dict()))
                self.expr.set(str(math.factorial(val)))
            elif key == 'MC':
                self.memory = 0
            elif key == 'MR':
                self.expr.set(self.expr.get() + str(self.memory))
            elif key == 'M+':
                self.memory += float(eval(self.expr.get(), self.safe_dict()) if self.expr.get() else 0)
            elif key == 'M-':
                self.memory -= float(eval(self.expr.get(), self.safe_dict()) if self.expr.get() else 0)
            else:
                self.expr.set(self.expr.get() + key)
        except Exception:
            messagebox.showerror('Error', 'Invalid Operation')

    def safe_dict(self):
        return {
            '__builtins__': None,
            'sin': lambda x: math.sin(math.radians(x)),
            'cos': lambda x: math.cos(math.radians(x)),
            'tan': lambda x: math.tan(math.radians(x)),
            'sqrt': math.sqrt,
            'log': math.log10,
            'pi': math.pi,
            'e': math.e,
            'abs': abs,
            'pow': pow
        }

    def calculate(self):
        result = eval(self.expr.get(), self.safe_dict())
        self.expr.set(str(result))

if __name__ == '__main__':
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()
