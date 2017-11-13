# encoding: utf-8
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    class Person(object):
        name = u'李长春'
        age = 33

    lcc = Person()



    countext = {
        'username': u'知了课堂',
        'age': 32,
        'person' : lcc,
        'websites': {
            'baidu':'www.baidu.com',
            'google':'www.google.com'
        }
    }
    return render_template('index.html',**countext)


if __name__ == '__main__':
    app.run(debug=True)