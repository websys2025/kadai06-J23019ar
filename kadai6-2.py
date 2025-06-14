import requests
import json

# ==========================================
# ファイル名：kadai6-2.py
#
# 【参照するオープンデータ】
# 気象庁 防災気象情報（天気予報・概況）
#
# 【データ名】
# 東京都の天気概況（overview_forecast）
#
# 【概要】
# 全国の地域ごとの天気概況をJSONで提供するオープンデータ。
# 地方コードにより、都道府県別の天気情報が取得できる。
#
# 【エンドポイント】
# https://www.jma.go.jp/bosai/forecast/data/overview_forecast/130000.json
#
# 【機能】
# - 東京都（130000）の最新の天気概況を取得し、コンソールに表示する。
#
# 【使い方】
# Pythonでこのプログラムを実行すると、東京都の天気概況が表示される。
# ==========================================

# 東京都の地域コード（130000）を指定してURLを構成
url = "https://www.jma.go.jp/bosai/forecast/data/overview_forecast/130000.json"

try:
    response = requests.get(url)
    response.raise_for_status()  # HTTPエラーがあれば例外発生
    data = response.json()

    # 必要な情報を抽出
    report_datetime = data["reportDatetime"]
    publishing_office = data["publishingOffice"]
    headline_text = data["headlineText"]
    text = data["text"]

    # 結果を表示
    print("【気象庁・東京都 天気概況】")
    print(f"発表機関：{publishing_office}")
    print(f"発表日時：{report_datetime}")
    if headline_text:
        print(f"見出し：{headline_text}")
    print("\n--- 概況 ---")
    print(text)

except requests.exceptions.RequestException as e:
    print("天気データの取得に失敗しました：", e)
except KeyError:
    print("想定外のデータ形式です。気象庁のデータ構造が変わった可能性があります。")
