import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Máy Tính Cơ Bản")
        master.geometry("400x500")
        master.resizable(False, False)

        # Tạo ô nhập liệu
        self.entry = tk.Entry(master, width=25, font=("Arial", 20), justify="right", bd=10, insertwidth=2, bg="powder blue")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Tạo các nút
        buttons = [
            "C", "⌫", "%", "/",
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "±", "0", ".", "="
        ]

        row = 1
        col = 0
        for button_text in buttons:
            if button_text in ["C", "⌫", "=", "±"]:
                tk.Button(master, text=button_text, width=5, height=2, font=("Arial", 14),
                          bg="light coral" if button_text == "C" else "light green",
                          command=lambda x=button_text: self.special_action(x)).grid(row=row, column=col, padx=5, pady=5)
            else:
                tk.Button(master, text=button_text, width=5, height=2, font=("Arial", 14),
                          bg="light gray",
                          command=lambda x=button_text: self.add_to_entry(x)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def add_to_entry(self, value):
        """Thêm giá trị vào ô nhập liệu"""
        self.entry.insert(tk.END, value)

    def special_action(self, action):
        """Xử lý các nút đặc biệt"""
        current_text = self.entry.get()
        if action == "C":
            self.entry.delete(0, tk.END)
        elif action == "⌫":
            self.entry.delete(len(current_text) - 1, tk.END)
        elif action == "±":
            try:
                if current_text.startswith('-'):
                    self.entry.delete(0, 1)
                else:
                    self.entry.insert(0, '-')
            except:
                pass
        elif action == "=":
            self.evaluate()

    def evaluate(self):
        """Đánh giá biểu thức toán học"""
        try:
            # Sửa dấu ± trong trường hợp người dùng nhập thủ công
            expression = self.entry.get().replace("±", "-")
            result = str(eval(expression))
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

# Khởi chạy ứng dụng
root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
