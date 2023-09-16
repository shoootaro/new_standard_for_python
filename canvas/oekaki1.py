import tkinter as tk

class Oekaki(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        # キャンパスサイズ
        self.canvas_width = 900
        self.canvas_height = 500

        # 線の色
        self.color = "black"
        # 線幅
        self.line_width = 3

        # マウスの位置
        self.px = 0
        self.py = 0
        # 最後に書いた線
        self.last_line = []
        # 全ての線
        self.all_lines = []
        # ツールバー
        self.create_toolbar()

        # キャンバス
        self.canvas = tk.Canvas(
            self, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()
        self.canvas.bind("<ButtonPress-1>", self.button_pressed)
        self.canvas.bind("<B1-Motion>", self.mouse_moved)
        self.canvas.bind("<ButtonRelease-1>", self.button_up)

    # ツールバーにウィジットを配置する
    def create_toolbar(self):
        # ツールバーを表示するフレーム
        self.toolbar = tk.Frame(self)
        self.toolbar.pack()
        # 色を選択するRadiobutton
        self.color_sel = tk.StringVar()
        self.color_sel.set(self.color)
        black = tk.Radiobutton(self.toolbar, text="黒",
                               variable=self.color_sel, value="black")
        black.pack(side=tk.LEFT)
        red = tk.Radiobutton(self.toolbar, text="赤",
                               variable=self.color_sel, value="red")
        red.pack(side=tk.LEFT)
        green = tk.Radiobutton(self.toolbar, text="緑",
                               variable=self.color_sel, value="green")
        green.pack(side=tk.LEFT)
        yellow = tk.Radiobutton(self.toolbar, text="黄",
                               variable=self.color_sel, value="yellow")
        yellow.pack(side=tk.LEFT)

        # 線幅を設定するOptionMenu
        self.line_var = tk.IntVar()
        self.line_var.set(self.line_width)
        line_ws = (1, 2, 3, 4, 5, 6, 7, 8)
        line_menu = tk.OptionMenu(self.toolbar, self.line_var, *line_ws)
        line_menu.pack(side=tk.LEFT)

        # 「取り消し」ボタン
        undo_btn = tk.Button(self.toolbar, text="取り消し", 
                                  command=self.undo)
        undo_btn.pack(side=tk.LEFT, padx=15)

    # マウスボタンが押された
    def button_pressed(self, event):
        self.px = event.x
        self.py = event.y
        # 線の色
        self.color = self.color_sel.get()
        # 線幅
        self.line_width = self.line_var.get()
        
    # マウスが動いた
    def mouse_moved(self, event):
        x = event.x
        y = event.y
        id = self.canvas.create_line(self.px, self.py, x, y, 
                                     fill = self.color, width=self.line_width)
        self.px = x
        self.py = y
        self.last_line.append()
    
    # ボタンが離された
    def button_up(self, event):
        self.all_lines.append(self.last_line)
        self.last_line = []
    
    # 最後に描いた線を取り消す
    def undo(self):
        if len(self.all_lines) > 0:
            last = self.all_lines.pop()
            for l in last:
                self.canvas.delete(l)

if __name__ == '__main__':
    root = tk.Tk()
    root.option_add("*font", "Courier 30")
    root.title("お絵かきアプリ")
    Oekaki(master=root)
    root.mainloop()

