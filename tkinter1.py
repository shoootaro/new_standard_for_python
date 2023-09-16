import tkinter as tk

# メインウィンドウ
root = tk.Tk()

# タイトル
root.title("初めてのtkinter")

# ウィンドウサイズ
# root.geometry("400x100")

# 最初のフレーム
frame1 = tk.Frame(root, bg = "gray", padx=10, pady=20)
frame1.pack()
# ラベル
label1 = tk.Label(frame1, text="ラベル１", bg="yellow")
label1.pack(side=tk.LEFT)
label2 = tk.Label(frame1, text="ラベル２", bg="azure")
label2.pack(side=tk.LEFT)

# ２番目のフレーム
frame2 = tk.Frame(root, bg = "lightblue", padx=10, pady=20)
frame2.pack()
# ラベル
label3 = tk.Label(frame2, text="ラベル３", bg="pink")
label3.pack(side=tk.LEFT)
label4 = tk.Label(frame2, text="ラベル４", bg="darkgray")
label4.pack(side=tk.LEFT)

# メインループ
root.mainloop()