import tkinter as tk

root = tk.Tk()
root.title("Textウィジットのテスト")

text = tk.Text(
    root,
    width=45,
    height=3
)
text.pack()

lines = """こんにちはPythonの世界へようこそ
tkinterでGUIプログラミング
WebAPIを使用する"""
text.insert("1.0", lines)

root.mainloop()