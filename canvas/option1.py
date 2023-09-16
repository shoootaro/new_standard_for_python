import tkinter as tk

root = tk.Tk()
root.title("OptionMenuのテスト")
root.geometry("300x200")

def change(value):
    # ラベルにvalueの値を表示
    label["text"] = value

nums = tk.IntVar()
items = (1, 2, 3, 4, 5, 6, 7, 8)
option_menu = tk.OptionMenu(root, nums, *items, command=change)
option_menu.pack()
nums.set(2)

label = tk.Label(root, text=nums.get(), font=("", 20), width=15)
label.pack()

root.mainloop()