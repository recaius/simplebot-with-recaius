from flask import Flask, request
import json, requests, os

app = Flask(__name__)

service_id = os.environ['RECAIUS_ID']
service_password = os.environ['RECAIUS_PASSWORD']
chat_token_granted_ja_en = os.environ['CHAT_TOKEN_JA_EN']

payload_to_get_token = {
    'machine_translation': {
        'service_id': service_id,
        'password': service_password
    }
}


def translate(message, trans_from, trans_to):
    r = requests.post('https://api.recaius.jp/auth/v2/tokens', json=payload_to_get_token)
    recaius_token = r.json()['token']

    payload_to_translate = {
        'mode': 'spoken_language',
        'query': message,
        'src_lang': trans_from,
        'tgt_lang': trans_to,
        'arrange': 'true'
    }

    trans = requests.post('https://api.recaius.jp/mt/v2/translate', headers={'X-Token': recaius_token},
                          json=payload_to_translate).json()

    requests.delete('https://api.recaius.jp/auth/v2/tokens', headers={'X-Token': recaius_token})

    return trans['data']['translations'][0]['translatedText']


@app.route('/ja_en', methods=['POST'])
def japanese_to_english():
    try:
        chat_token = request.form['token']
        print("chat token: " + chat_token)
        if chat_token != chat_token_granted_ja_en:
            return
    except:
        chat_token = ""

    try:
        in_text = request.form['text']
    except:
        in_text = ""

    result = translate(in_text, 'ja', 'en')

    payload_to_chat = {
        'text': 'text: ' + result,
        'MATTERMOST_TOKEN': chat_token
    }

    return json.dumps(payload_to_chat)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
