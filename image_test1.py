import tkinter as tk

# メインウインドウ
root = tk.Tk()
# フレーム
frame = tk.Frame(root)
frame.pack()

# PhotoImageオブジェクトを生成
my_image = tk.PhotoImage(file="images/radio1.png")
# ラベルに表示
label = tk.Label(frame, image=my_image)
label.pack()

root.mainloop()