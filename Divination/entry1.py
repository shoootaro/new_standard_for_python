import tkinter as tk

# メインウィンドウ
root = tk.Tk()
# タイトル
root.title("Entryのテスト")
# ウィンドウサイズ
root.geometry("400x100")

def get_text():
  # getメソッドを使用して文字列を取得
  label["text"] = str_var.get()

def set_text():
  # setメソッドを使用して文字列を設定
  str_var.set("こんにちは")
  
# StringVarオブジェクトを生成
str_var = tk.StringVar()

# Entryを生成し、変数strとEntryウィジェットの文字列を関連付ける
entry = tk.Entry(root, width=20, textvariable=str_var)
entry.pack()
button1 = tk.Button(root, text="取得", command=get_text)
button1.pack(side=tk.LEFT)
button2 = tk.Button(root, text="設定", command=set_text)
button2.pack(side=tk.LEFT)
# ラベル
label = tk.Label(root, text="")
label.pack(side=tk.LEFT)
# メインループ
root.mainloop()