import tkinter as tk

# メインウィンドウ
root = tk.Tk()

# タイトル
root.title("ボタンテスト")

def clicked():
    print("ボタンがクリックされました")

btn1 = tk.Button(root, text="押してください", command=clicked, bg="yellow")
btn1.pack()

# メインループ
root.mainloop()