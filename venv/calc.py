import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
WHITE = "#FFFFFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        self.total_expression = ""
        self.current_expression = "0"
        self.display_frame = self.create_display_frame()
        
        self.total_label, self.label = self.create_display_labels()
        
        self.digits = {
            7: (1, 0), 8: (1, 1), 9: (1, 2),
            4: (2, 0), 5: (2, 1), 6: (2, 2),
            1: (3, 0), 2: (3, 1), 3: (3, 2),
            0: (4, 1), '.': (4, 0), '00': (5, 1)  # Double zero button in last row
        }
        self.operations = {
            '+': (5, 2), '-': (4, 2),
            '*': (3, 3), '/': (2, 3),
            'C': (5, 0),  # Clear button
            '<-': (1, 3),  # Backspace button
            '%': (4, 3),   # Modulo button
            '=': (5, 3)    # Equal sign in last row, last column
        }
        self.buttons_frame = self.create_buttons_frames()
        self.create_digit_buttons()
        self.create_operation_buttons()

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill="both")

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(
                self.buttons_frame,
                text=str(digit),
                bg=WHITE,
                fg=LABEL_COLOR,
                command=lambda d=digit: self.add_to_expression(d),
                width=10,
                height=3
            )
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_operation_buttons(self):
        for operation, grid_value in self.operations.items():
            button = tk.Button(
                self.buttons_frame,
                text=operation,
                bg=WHITE,
                fg=LABEL_COLOR,
                command=lambda op=operation: self.handle_operation(op),
                width=10,
                height=3
            )
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_buttons_frames(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        
        for i in range(6):  # 6 rows
            frame.grid_rowconfigure(i, weight=1)
        for j in range(4):  # 4 columns
            frame.grid_columnconfigure(j, weight=1)

        return frame

    def add_to_expression(self, value):
        if self.current_expression == "0":
            self.current_expression = str(value)
        else:
            self.current_expression += str(value)
        self.update_display()

    def handle_operation(self, operation):
        if operation == "C":
            self.current_expression = "0"
            self.total_expression = ""
        elif operation == "<-":  # Backspace functionality
            if len(self.current_expression) > 1:
                self.current_expression = self.current_expression[:-1]
            else:
                self.current_expression = "0"
        elif operation == "=":
            try:
                self.current_expression = str(eval(self.total_expression + self.current_expression))
                self.total_expression = ""
            except Exception:
                self.current_expression = "Error"
        else:
            if self.current_expression != "0":
                self.total_expression += self.current_expression + operation
                self.current_expression = "0"
        self.update_display()

    def update_display(self):
        self.label.config(text=self.current_expression)
        self.total_label.config(text=self.total_expression)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
