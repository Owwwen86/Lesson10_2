# -*- coding: cp1251 -*-
from flask import Flask
from functions import load_candidates, get_all, get_by_pk, get_by_skill

FILENAME = 'candidates.json'
data = get_all(load_candidates(FILENAME))
app = Flask(__name__)


@app.route("/")
def page_index():
    str = '<pre>'
    for i in data:
        str += f'{i} \n'
    str += '</pre>'
    return str


@app.route("/candidates/<int:pk>")
def page_candidates(pk):
    user = get_by_pk(pk, data)
    if user:
        str = f'<img src="{user.picture}">'
        str += f'<pre>{user} </pre>'
    else:
        str = 'NO FOUND'
    return str


@app.route("/skills/<x>")
def page_skills(x):
    x = x.lower()
    users = get_by_skill(x, data)
    if users:
        str = f'<pre>'
        for i in users:
            str += f'{i} \n'
        str += '</pre>'
    else:
        str = 'NO FOUND'
    return str


if __name__ == '__main__':
    app.run(host='127.0.0.2', port=800)
