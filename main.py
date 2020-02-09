
# import logging

from flask import Flask,  request, render_template
from google.cloud import translate

import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def landing_page():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Translate':
            text_input = request.form['text']
            client = translate.Client()
            translate_dict = client.translate(text_input)
            result_translate = json.dumps(translate_dict, sort_keys=False, indent=2)
            return render_template('index.html', result=result_translate)
        elif request.form['submit_button'] == 'Detect':
            text_input = request.form['text']
            client = translate.Client()
            detect_dict = client.detect_language(text_input)
            result_detect = json.dumps(detect_dict, sort_keys=False, indent=2)
            return render_template('index.html', result=result_detect)
        else:
            pass
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
