import tkinter as tk
import os
import random

def uranau():
    # 占いを実行する
    show_kuji["image"] = random.choice(kujis)

def clear():
    # 占いをクリアする
    show_kuji["image"] = default_img

# メインウインドウ
root = tk.Tk()

# タイトル
root.title("おみくじ")

# デフォルトのイメージの読み込み（パスの相違を吸収）
default_img = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "kujis/empty.png"))

# ４つのクジのイメージファイル
kujis = [tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "kujis/kyo.png")),
    tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "kujis/syoukiti.png")),
    tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "kujis/chukiti.png")),
    tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "kujis/daikiti.png"))]

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
show_kuji = tk.Label(root, image=default_img)
show_kuji.pack()

# メインループ
root.mainloop()
