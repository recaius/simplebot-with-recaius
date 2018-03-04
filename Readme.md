Recaiusにより口語翻訳を行う簡易ボット(Slack / Mattermost用)
====

日英翻訳を行なう例です。
他の翻訳を行なうには、それぞれ同様にエンドポイントを追加し、WebHookの設定を行ないます。


Slack / Mattermostの設定
----

外向きの WebHookを設定します。

1. コンテントタイプは「application/x-www-form-urlencoded」
1. トリガーワードは「翻訳」など
1. コールバックURLは「 https://simplebot:5000/ja_en 」など、
「/ja_en」をエンドポイントとして下さい。


ローカル PC上での実行手順
----

```bash
git clone https://github.com/recaius/simplebot-with-recaius.git
cd simplebot-with-recaius
virtualenv . -p python3
. bin/activate
pip install flask requests

export RECAIUS_ID=''        # お使いの RECAIUSの ID
export RECAIUS_PASSWORD=''  # お使いの RECAIUSのパスワード
export CHAT_TOKEN_JA_EN=''  # Slack / Mattermostで設定したトークン

python simplebot.py
```


Dockerでの実行手順
----

```bash
cd docker
vi Dockerfile  # 上記の3つの環境変数を設定して下さい。

docker build . -t simplebot
docker run -d -p 5000:5000 simplebot
```


Herokuでの実行手順
----

事前に Herokuのアカウント作成や CLIのインストールを行って下さい。
Herokuでの実行に必要な設定は含んでいます。
Heroku上のアプリ名(simplebot-xxxxx の部分)は重複しない様に変更してください。

```bash
heroku login
heroku create simplebot-xxxxx

# ここで Herokuサーバの管理コンソール上で上記3つの環境変数を設定してください。

git push heroku master

heroku logs  # 正常に起動したか確認します。
```


動作確認
----

Slack / Mattermostから以下の様に発言(「」部分)します。

```
<あなたの名前>
「翻訳 私はカモメ」
```

以下の様に回答があれば動作しています。

```
<Recaius [BOT]>
「I am a sea gull.」
```

以上。
