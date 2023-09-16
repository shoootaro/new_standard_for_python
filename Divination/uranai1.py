import tkinter as tk
import random

def uranau():
    # 占いを実行する
    show_kuji["text"] = random.choice(kujis)

def clear():
    # 占いをクリアする
    show_kuji["text"] = ""

# メインウインドウ
root = tk.Tk()

# タイトル
root.title("おみくじ")

# くじの中身
kujis = ["大吉", "中吉", "小吉", "凶"]

# ボタンを配置するフレーム
btn_frame = tk.Frame(root, padx=10, pady=20)
btn_frame.pack()

# 占うボタン
uranau_btn = tk.Button(btn_frame, text="占う", command=uranau, bg="lightblue")
uranau_btn.pack(side='left')

# クリアボタン
clear_btn = tk.Button(btn_frame, text="クリア", command=clear, bg="yellow")
clear_btn.pack(side='left')

# 占い結果を表示するラベル
show_kuji = tk.Label(root, image="", font=("Helvetica", 30, "bold"))
show_kuji.pack()

# メインループ
root.mainloop()