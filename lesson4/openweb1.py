import tkinter as tk
import webbrowser

root = tk.Tk()
root.geometry("200x100")

url = "https://google.co.jp"
button = tk.Button(root, text="オープンWeb", command=lambda: webbrowser.open(url))
button.pack()

root.mainloop()