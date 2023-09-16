import tkinter as tk

root = tk.Tk()
root.title="Canvasのテスト"

canvas = tk.Canvas(root, width=500, height=300)
canvas.pack()

canvas.create_line(10, 10, 400, 40, width=10, fill="lightblue")
canvas.create_rectangle(400, 50, 450, 200, fill="green",
                        outline="purple", width=15)
canvas.create_oval(10, 50, 400, 200, fill="yellow",
                   outline="blue", width=10)
canvas.create_text(250, 250, text="キャンバスのテスト", font=("", 30))

tk.mainloop()