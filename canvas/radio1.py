import tkinter as tk

root = tk.Tk()
root.title("RadioButtonのテスト")

def change():
    # ラベルにvalueの値を表示
    label["text"] = rg.get()

r_frame = tk.Frame(root)
r_frame.pack()

# IntVarオブジェクトを用意する
rg = tk.IntVar()
# IntVarオプションに初期として3を設定
rg.set(3)

# 4つのラジオボタンを生成する
radio1 = tk.Radiobutton(r_frame, text="春",
                        variable=rg, value=1, command=change)
radio1.pack(side=tk.LEFT)
radio2 = tk.Radiobutton(r_frame, text="夏",
                        variable=rg, value=2, command=change)
radio2.pack(side=tk.LEFT)
radio3 = tk.Radiobutton(r_frame, text="秋",
                        variable=rg, value=3, command=change)
radio3.pack(side=tk.LEFT)
radio4 = tk.Radiobutton(r_frame, text="冬",
                        variable=rg, value=4, command=change)
radio4.pack(side=tk.LEFT)

label = tk.Label(root, text=rg.get(), font=(", 20"), width=15)
label.pack()

root.mainloop()