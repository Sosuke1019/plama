# plama
![This is an image](https://github.com/Sosuke1019/plama/blob/main/static/images/plama_indexpage.png)

## Overview
寮でモノ（家具、食材、服...）をラクに引き継ぐ事を可能にするフリマサービス。

## Description
- ペルソナ <br>
1年間の留学のため、引越しの時期に家具や服を他の寮生に引き継ぎたいと考える寮に住む留学生。友人は1～3名で、さらに友人も同じタイミングで引っ越しをするので、引き継ぐ人がいない。捨てるのは勿体無いけど、わざわざ他の寮生に聞いたりしたくはない。
- 解決出来る問題 <br>
上記のペルソナを持った留学生が複数いた場合、グループLINEでは情報をまとめにくい。1つのwebサービスに情報を集約する事で、寮生は貰い手を募集しやすく、貰い手側も情報を探しやすくなる。また、引越しの時期は3週間程度のため、わざわざinstallはしなくてもwebアプリケーションとして利用出来る。
- 仕組みを一言で説明 <br>
ユーザー登録をする事で誰でも自由にモノを出品する事ができる。

## Requirement
- ubuntu 20.04.5 
- Python 3.8.10
- Flask 2.2.3
- Werkzeug 2.2.3

## Getting Started

## Features
Video Demo: [Youtube](https://github.com/Sosuke1019) <br>

### 要件定義 
- 新規登録
- ログイン機能
	- 名前/部屋番号/パスワード
- ログアウト機能
- index画面で出品されたモノを一覧できる
- 出品画面でモノを出品できる
	- 写真/商品の名前/商品の説明
-  編集画面から出品したモノを削除できる

### 使用技術
- フロントエンド：HTML, CSS, Bootstrap
- フレームワーク：Flask
- DB：SQLite3
- webサーバー：Nginx
- アプリケーションサーバー：gunicorn
- 開発環境：Github

### 今後実装したい機能
- VPSを契約して、ドメインも取得したがNginxとgunicornの実装に時間がかかってしまったため、デプロイ出来ていない。よって、提出後にデプロイまで行う
- アカウント削除機能を付ける
- 現在は商品の一覧が表示されるだけだが、商品を選択してアプリケーション内で取引が成立するようにする。
- 出品した商品が購入された場合、メール通知が来るようにする。
- お気に入り機能

## Reference
- https://bootstrap-guide.com/layout/columns
- https://qiita.com/tomo0/items/a762b1bc0f192a55eae8
- https://qiita.com/Kotabrog/items/fb328b72ac94137897af

## Author
[GitHub](https://github.com/Sosuke1019)
