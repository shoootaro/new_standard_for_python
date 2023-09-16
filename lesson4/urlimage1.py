import tkinter as tk
from PIL import Image, ImageTk
import requests

# メインウィンドウ
root = tk.Tk()
# タイトル
root.title("インターネット上のイメージを取得")

URL = "https://o2-m.com/lake1.jpg"
img = requests.get(URL).content
photo = ImageTk.PhotoImage(data=img)

label = tk.Label(image=photo)
label.pack()

root.mainloop()