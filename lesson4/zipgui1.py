import requests
import tkinter as tk

class ZipSearch(tk.Frame):
    zipapi = "https://zipcloud.ibsnet.co.jp/api/search"

    def __init__(self, master=None):
        super().__init__(master, bg="lightblue", padx=20, pady=20)
        self.pack(fill=tk.BOTH)

        # 検索用フレーム
        self.search_frame = tk.Frame(self, pady=10, padx=5)
        self.search_frame.pack()

        # 入力テキスト（郵便番号）用変数
        self.zip_entry_var = tk.StringVar()
        # 数字以外は入力できないようにする
        val_cmd = master.register(self.validate_digit)
        
        # 入力テキスト用Entry
        self.zip_entry = tk.Entry(self.search_frame, 
                                  validate="key",
                                  validatecommand=(val_cmd, "%S","%P",),
                                  textvariable=self.zip_entry_var)
        self.zip_entry.pack(side='left')

        # 「検索」ボタン
        self.search_button = tk.Button(self.search_frame, text="検索", command=self.search)
        self.search_button.pack(side='left')
        self.search_button["state"] = "disabled"

        # 結果表示用のラベル
        self.result_label = tk.Label(self, bg="lightblue", font=("", 18))
        self.result_label.pack(fill=tk.X)
    
    def validate_digit(self, char, entry_str):
        if char.isdigit():
            if len(entry_str) == 7:
                self.search_button["state"] = "normal"
            else:
              self.search_button["state"] = "disabled"
            return True
        else:
            return False

    def search(self):
        zipcode = self.zip_entry_var.get()

        # 郵便番号APIを呼び出してJSONデータを取得する
        params = {"zipcode" : zipcode}
        result = requests.get(ZipSearch.zipapi, params=params).json()

        # ステータスコードのチェック
        if result["status"] != 200:
            self.result_label["text"] = result["message"]
        else:
            # 住所が見つかったかどうかをチェック
            if result["results"]:
                # 結果をラベルに表示
                self.result_label["text"] = result["results"][0]["address1"] + \
                result["results"][0]["address2"] + result["results"][0]["address3"]
            else:
                self.result_label["text"] = "見つかりません"

if __name__ == '__main__':
    root = tk.Tk()
    root.title("郵便番号検索API")
    root.geometry("480x150")
    root["bg"] = "lightblue"
    app = ZipSearch(master=root)
    root.mainloop()