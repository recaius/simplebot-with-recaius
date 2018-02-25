from flask import Flask, request
import json

app = Flask(__name__)


# Mattermost トークン: ht8gw8m13jrhde6iqr9597fsur
@app.route('/to_en', methods=['POST'])
def translate_to_english():
    print(request.form)

    try:
        token = request.form['token']
        print("token: " + token)
    except:
        token = ""

    try:
        inText = request.form['text']
    except:
        inText = ""

    payload = {
        'text': 'text: ' + inText,
        'MATTERMOST_TOKEN': token
    }

    return json.dumps(payload)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
