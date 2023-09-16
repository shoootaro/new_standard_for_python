import tkinter as tk
import random

root = tk.Tk()
root.title("Canvasのテスト")

# コールバック関数
def button_pressed(event):
    size = random.randint(50,100)
    canvas.create_rectangle(event.x - size, event.y - size,
                            event.x + size, event.y + size,
                            outline="green", width=5)

# Canvasを生成する
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# Canvasをクリックするとbutton_pressedを呼び出す
canvas.bind("<ButtonPress-1>", button_pressed)

root.mainloop()