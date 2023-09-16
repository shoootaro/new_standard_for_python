import requests

zipapi = "https://zipcloud.ibsnet.co.jp/api/search"
zcode = input("郵便番号を入力してください : ")
params = {"zipcode" : zcode}
r = requests.get(zipapi, params=params)
zip_json = r.json()

if zip_json["status"] != 200:
    print(zip_json["message"])
else:
    if zip_json["results"]:
        print(zip_json["results"])
    else:
        print("見つかりません")