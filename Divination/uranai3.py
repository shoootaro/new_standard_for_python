import tkinter as tk
import os.path
import random

class Uranai(tk.Frame):
    def __init__(self, master):
        super().__init__(master, padx=10, pady=10)
        self.pack()
        # ボタンを配置するフレーム
        self.btn_frame = tk.Frame(self, padx=10, pady=20)
        self.btn_frame.pack()
        # 「占う」ボタン
        self.uranau_btn = tk.Button(self.btn_frame, text="占う", command=self.uranau)
        self.uranau_btn.pack(side='left')
        # 「クリア」ボタン
        self.clear_btn = tk.Button(self.btn_frame, text="クリア", command=self.clear)
        self.clear_btn.pack(side='left')

        # デフォルトのイメージの読み込み（ディレクトリの相違を吸収）
        self.default_img = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "kujis/empty.png"))
        # くじの４つのイメージファイル
        self.kujis = [
            tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "kujis/kyo.png")),
            tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "kujis/syoukiti.png")),
            tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "kujis/chukiti.png")),
            tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "kujis/daikiti.png")),
            ]
        # 占い結果を表示するラベル
        self.show_kuji = tk.Label(self, image=self.default_img)
        self.show_kuji.pack()
    
    def uranau(self):
        # 占いを実行する
        self.show_kuji["image"] = random.choice(self.kujis)
    
    def clear(self):
        self.show_kuji["image"] = self.default_img
    
if __name__ == '__main__':
    # メインウィンドウ
    root = tk.Tk()
    # タイトル
    root.title("おみくじ")
    app = Uranai(root)
    # メインループ
    root.mainloop()