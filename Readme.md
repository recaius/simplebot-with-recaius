Recaiusにより口語翻訳を行う簡易ボット(Slack / Mattermost用)
====

実行手順
----

```
export RECAIUS_ID=''
export RECAIUS_PASSWORD=''
export CHAT_TOKEN_JA_EN=''

git clone https://github.com/recaius/simplebot-with-recaius.git
cd simplebot-with-recaius
virtualenv . -p python3
pip install flask
python simplebot.py
```

以上。