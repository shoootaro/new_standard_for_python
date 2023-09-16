import tkinter as tk
import os.path
import pickle

class Item(tk.Frame):
    # 個々のtodo項目
    def __init__(self, main, todo_text, checked):
        super().__init__(main, bg="lightblue", padx=10, pady=5)
        self.pack(fill=tk.X)
        self.main = main

        # todoテキストを設定
        self.item_text = todo_text

        # チェックボックス用のウィジット変数を設定
        self.chk_v = tk.BooleanVar()
        self.chk_v.set(checked)

        # チェックボックス
        self.chk = tk.Checkbutton(self,
                                  variable = self.chk_v,
                                  command = self.show_delbtn,
                                  bg = "cyan")
        self.chk.pack(side=tk.LEFT)
        
        # todoテキスト
        self.txt = tk.Label(self, text=self.item_text, width=35)
        self.txt.pack(side=tk.LEFT)

        # 削除ボタン
        self.del_button = tk.Button(self,
                                    text="削除",
                                    command=self.del_item)
        
        # チェックボックスがチェックされていれば「削除」ボタンを表示
        if self.chk_v.get():
            self.del_button.pack(side=tk.LEFT)
    
    # アイテムを削除
    def del_item(self):
        self.destroy() # フレームを削除
        self.main.todo_items.remove(self)
        self.main.save_items()
    
    # チェックボックスがオンの場合に「削除」ボタンを表示
    def show_delbtn(self):
        if not self.chk_v.get():
            self.checked = False
            self.del_button.pack_forget()
        else:
            self.checked = True
            self.del_button.pack(side=tk.RIGHT)
        self.main.save_items() # Todoリストを保存

class Todo(tk.Frame):
    # データ保存先のパス
    data_file_path = os.path.join(os.path.dirname(__file__), "todo.data")

    def __init__(self, master=None):
        super().__init__(master, bg="yellow", padx=10, pady=20)
        master["bg"] = "yellow"
        self.pack()

        # 空のtodoリストを生成
        self.todo_items = []

        # 入力フォーム用のフレーム
        self.enter_frame = tk.Frame(self, padx=2, pady=20, bg="yellow")
        self.enter_frame.pack()

        # 入力テキスト用のウィジット変数
        self.entry_var = tk.StringVar()

        # todo用のEntry
        val_cmd = master.register(self.validate_item)
        self.entry = tk.Entry(self.enter_frame,
                              textvariable=self.entry_var,
                              width="30",
                              validate="key",
                              validatecommand=(val_cmd, "%P")
                              )
        self.entry.pack(side='left')

        # 「追加」ボタン
        self.add_button = tk.Button(self.enter_frame,
                                    text="追加",
                                    command=self.add_item,
                                    state="disabled"
                                    )
        self.add_button.pack(side='left')

        # todoリストをファイルから読み込む
        self.load_items()

    # 入力テキストの検証
    def validate_item(self, val):
        if len(val) < 2:
            self.add_button["state"] = "disabled"
        else:
            self.add_button["state"] = "normal"
        return True

    # todo項目を追加
    def add_item(self):
        item_text = self.entry_var.get()
        self.todo_items.append(Item(self, item_text, False))
        self.save_items()
        self.entry_var.set("")
    
    # todoリストをファイルに保存
    def save_items(self):
        todos = []
        for item in self.todo_items:
            todos.append([item.item_text, item.chk_v.get()])
        out_file = open(Todo.data_file_path, "wb")
        pickle.dump(todos, out_file)
    
    # todoリストをファイルから読み込む
    def load_items(self):
        if os.path.exists(Todo.data_file_path):
            in_file = open(Todo.data_file_path, "rb")
            todos = pickle.load(in_file)
            for todo in todos:
                self.todo_items.append(Item(self, todo[0], todo[1]))

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Todoリスト")
    root.geometry("500x400")
    app = Todo(master=root)
    root.mainloop()


