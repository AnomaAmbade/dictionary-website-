from flask.templating import render_template
import requests
from pprint import pprint
from flask import Flask, render_template, request

URL = 'https://owlbot.info/api/v4/dictionary'
API_TOKEN = 'YOUR_API_TOKEN'

header = {
    'Authorization': f'Token {API_TOKEN}',
}


app = Flask(__name__)

# home route
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        word = request.form['word']
        response = requests.get(url=f'{URL}/{word}', headers=header)
        res_json = response.json()
        pprint(res_json)
        return render_template('index.html', response=res_json)
    else:
        return render_template('index.html', response='')


if __name__ == '__main__':
    app.run(debug=True)

