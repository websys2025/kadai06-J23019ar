import requests
import json

# ============================
# e-Stat APIを使って都道府県別平均寿命データを取得するプログラム
# ファイル名：kadai6-1.py
#
# 【取得するデータ】
# ・簡易生命表（令和2年）
# ・都道府県別の平均寿命（男女別）
#
# 【使用APIエンドポイント】
# https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData
#
# 【統計表ID（statsDataId）】
# 0003427428
#
# 【使い方】
# Pythonでこのファイルを実行すると、都道府県ごとの平均寿命（男女）が表示される。
# ============================

# APIキー（e-Statのマイページで取得したAPIキーを使用すること）
API_KEY = "59abe64c9c15fc5e26baf8977450bbc48b6a8804"

# APIエンドポイント
url = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

# APIパラメータ
params = {
    "appId": API_KEY,
    "statsDataId": "0003427428",  # 簡易生命表（令和2年）
    "lang": "J",  # 日本語
}

# APIリクエストを送信
response = requests.get(url, params=params)

# JSONデータをパース
data = response.json()

# エラーチェック
if "GET_STATS_DATA" not in data or "STATISTICAL_DATA" not in data["GET_STATS_DATA"]:
    print("データの取得に失敗しました。APIキーやstatsDataIdを確認してください。")
    exit()

# データ本体にアクセス
values = data["GET_STATS_DATA"]["STATISTICAL_DATA"]["DATA_INF"]["VALUE"]

# 都道府県別の平均寿命データを抽出
lifespan_data = {}

for item in values:
    pref_name = item["@area"]        # 都道府県名
    gender = item["@cat01"]          # 性別 (男A1301、女A1302)
    value = item["$"]                # 平均寿命

    if pref_name not in lifespan_data:
        lifespan_data[pref_name] = {}

    if gender == "A1301":
        lifespan_data[pref_name]["男"] = value
    elif gender == "A1302":
        lifespan_data[pref_name]["女"] = value

# 平均寿命データを表示
print("都道府県別 平均寿命（令和2年）")
print("-----------------------------")
for pref in sorted(lifespan_data.keys()):
    male = lifespan_data[pref].get("男", "N/A")
    female = lifespan_data[pref].get("女", "N/A")
    print(f"{pref}: 男 {male} 歳 / 女 {female} 歳")
