import tkinter as tk

# メインウィンドウ
root = tk.Tk()
# タイトル
root.title("Entryの検証1")
# ウィンドウサイズ
root.geometry("400x100")

# 検証用の関数
def validate_entry(chr):
    if chr.isdigit():
        return True
    else:
        return False

# SrtingVarオブジェクトを生成
strVar = tk.StringVar()

# 検証用の関数を登録
val_cmd = root.register(validate_entry)
# Entry
entry = tk.Entry(root, width=20, textvariable=strVar,
                 validatecommand=(val_cmd, "%S"),
                 validate="key")
entry.pack()

# メインループ
root.mainloop()