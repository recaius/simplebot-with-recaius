Recaiusにより口語翻訳を行う簡易ボット(Slack / Mattermost用)
====

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

```bash
heroku login
heroku create simplebot-xxxxx

# ここで Heroku上で上記3つの環境変数を設定してください。

git push heroku master

heroku logs  # 正常に起動したか確認します。
```


以上。
