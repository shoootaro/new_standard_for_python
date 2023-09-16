import tkinter as tk

# メインウィンドウ
root = tk.Tk()
# タイトル
root.title("チェックボックス")
# ウィンドウサイズ
root.geometry("200x100")

def get_chk():
    # getメソッドを使用してチェックボックスの状態取得
    label["text"] = str(bool_var.get())

# booleanVarオブジェクトを生成
bool_var = tk.BooleanVar()
# 初期状態でオフ
bool_var.set(False)

# チェックボックスを生成する
chkbox = tk.Checkbutton(root, variable=bool_var, text="チェックボックス", command=get_chk)
chkbox.pack()

# ラベル
label = tk.Label(root, text="False")
label.pack(side=tk.LEFT)

# メインループ
root.mainloop()