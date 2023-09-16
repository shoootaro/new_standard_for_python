import tkinter as tk

# メインウィンドウ
root = tk.Tk()

# フレーム
frame = tk.Frame(root)
frame.pack()

# PhotoImagepオブジェクトを作成
my_image = tk.PhotoImage(file="images/radio1.png")

# ラベルへ表示
label = tk.Label(frame, image=my_image)
label.pack()

# メインループ
tk.mainloop()