import tkinter as tk
import os
from PIL import Image, ImageTk

# メインウィンドウ
root = tk.Tk()
# タイトル
root.title("Pollowのテスト")

file_path = os.path.join(os.path.dirname(__file__), "images/bird.jpg")
photo_pil = Image.open(file_path)
photo_tk = ImageTk.PhotoImage(photo_pil)
label = tk.Label(image=photo_tk)
label.pack()

# メインループ
root.mainloop()
