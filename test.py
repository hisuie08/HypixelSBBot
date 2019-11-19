import json
import requests

key = "<API key>"
name = "<Player Name>"
profile_name = "<Profile Name>"

def get_profile_id(key,name, profile_name):  #プロファイル名からプロファイルIDを探すための関数です。
    data = requests.get(f"https://api.hypixel.net/player?key={key}&name={name}", headers={"content-type": "application/json"}).json()
    profiles = (data["player"]["stats"]["SkyBlock"]["profiles"])
    for profs in profiles.values():
        if (profs["cute_name"]) == profile_name:
            return profs["profile_id"]
    raise ValueError  #私のBOTでは利用登録の際この関数で返ってくるValueErrorが重要になるので敢えて分けていますが、特に理由がなければget_endpoint_urlに組み込んでも問題ありません。

def get_response(endpoint, key, name, profile_name):  #レスポンス取得関数。fork元コードでは叩いていた3つエンドポイントのURLスキームを構築してレスをjsonで受け取ります。
    profile_id = get_profile_id(key,name,profile_name)
    if endpoint == "auction":  #文字列が長くなってくると+の使用は可読性を下げるためf""を利用した方がいいそうです。変数の格納は{}。
        url = str(f"https://api.hypixel.net/skyblock/{endpoint}?key={key}&name={name}&profile={profile_id}")
    elif endpoint == "news":
        url = str(f"https://api.hypixel.net/skyblock/{endpoint}?key={key}")
    elif endpoint == "profile":
        url = str(f"https://api.hypixel.net/skyblock/{endpoint}?key={key}&profile={profile_id}")
    else:
        pass
    data = requests.get(url, headers={"content-type": "application/json"}).json()
    return data  #このdataをBOTの処理なりprinなりファイルなり、別の処理関数に渡して好きに加工できます。

def main(key, name, profile_name):  #get_responseで受け取ったデータを料理するメインの処理。例としてエンドポイントをfor回してprintと書き込みしてます。
    endpoints = ["profile", "auction", "news"]
    for endpoint in endpoints:
        data = get_response(endpoint, key, name, profile_name)
        print(json.dumps(data, indent=2))
        with open(f"{name}_{profile_name}_{endpoint}.json", "w") as f:
            json.dump(data,f,indent=2)#jsonの書き込みはwrite関数ではなくdump関数を使います。引数にjsonデータとファイルパス、インデント等指定します。


if __name__ == "__main__":
    main(key,name,profile_name)