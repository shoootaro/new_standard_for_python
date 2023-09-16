import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import webbrowser
import requests

class ContentFrame(tk.Frame):
    # 個々の検索結果表示用のフレーム
    def __init__(self, master, id, title, desc, img):
        super().__init__(master, bg="lightblue", padx=10, pady=10)
        self.pack(fill=tk.X)
        self.img_url = img

        self.video_id = id
        self.youtube_url = "https://www.youtube.com/watch?v=" + self.video_id
        self.title = title
        self.description = desc

        # サムネイル画像を生成
        img = requests.get(self.img_url).content
        self.tk_img = ImageTk.PhotoImage(data=img)

        # イメージ表示用ラベル
        self.img_label = tk.Label(self, image=self.tk_img)
        self.img_label.pack(side=tk.LEFT)

        # イメージにリンク設定
        self.img_label.bind(
          "<Button-1>", lambda e: webbrowser.open(self.youtube_url)
        )

        # タイトルと詳細表示用のフレーム
        self.text_frame = tk.Frame(self)
        self.text_frame.pack(fill=tk.X, padx=10, pady=10)
        # タイトル表示用ラベル
        self.title_Label = tk.Label(
            self.text_frame, text=self.title, font=("", 15, "bold")
        )
        self.title_Label.pack()

        # 詳細表示用Text
        self.desc_text = tk.Text(
            self.text_frame,
            width=45,
            height=3,
        )
        self.desc_text.pack()
        self.desc_text.insert("1.0", self.description)

class YoutubeSearch(tk.Frame):
    # YouTube APIを検索する
    def __init__(self, master=None):
        self.youtube_api = "https://www.googleapis.com/youtube/v3/search"
        # APIキーを作成
        self.apikey = "AIzaSyBJWXDWje2MJjLj5iN5FOFJf89g5GW9B6U"
        super().__init__(master, bg="lightblue", padx=20, pady=10)
        self.pack(fill=tk.X)

        # 検索テキストと「検索」ボタン用フレーム
        self.search_frame = tk.Frame(self, pady=10, padx=15)
        self.search_frame.pack()

        # 検索テキスト用の変数
        self.keyword_entry_var = tk.StringVar()

        # 検索キーワード用のEntry
        self.keyword_entry = tk.Entry(self.search_frame,
                                      textvariable=self.keyword_entry_var)
        self.keyword_entry_var.set("Giulietta Machine")
        self.keyword_entry.pack(side='left')

        # 「検索」ボタン
        self.search_button = tk.Button(self.search_frame,
                                       text="検索",
                                       command=self.search)
        self.search_button.pack(side='left')
        # 「クリア」ボタン
        self.clear_button = tk.Button(self.search_frame,
                                      text="クリア",
                                      command=self.clear)
        self.clear_button.pack(side='left')

        # 結果表示用のフレーム
        self.result_frame = tk.Frame(self, bg="lightblue", pady=2)
        self.result_frame.pack(fill=tk.Y)

        # 検索結果を格納するリスト
        self.search_results = []

    def clear(self):
        # 検索結果をクリアする
        for item in self.search_results:
            item.destroy()
        self.search_results = []
        print(len(self.search_results))
    
    def search(self):
        # 検索を実行する
        self.clear()

        # 検索キーワードを取得
        keyword = self.keyword_entry_var.get()

        # キーワードの入力がない場合にはエラー
        if len(keyword) == 0:
            messagebox.showerror("エラー", "検索キーワードを入力してください")
            return
        
        # クエリパラメタ
        params = {"part": "snippet", "q": keyword, "type": "video", "maxResults": "6", "key": self.apikey}

        # リクエストを送信して結果を取得
        results = requests.get(self.youtube_api, params=params).json()

        if len(results["items"]) == 0:
            messagebox.showerror("エラー", "見つかりません")
            return
        
        # 検索結果をひとつずつ取り出しContentFrameを生成して表示する
        for item in results["items"]:
            id = item["id"]["videoId"]
            title = item["snippet"]["title"]
            desc = item["snippet"]["description"]
            img = item["snippet"]["thumbnails"]["default"]["url"]
            self.search_results.append(ContentFrame(
                self.result_frame, id, title, desc, img))
            
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("700x800")
    root["bg"] = "lightblue"
    root.title("YouTube検索")
    app = YoutubeSearch(master=root)
    root.mainloop()