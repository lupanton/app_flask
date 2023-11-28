from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Main page'

@app.route('/name/<id>')
def name(id):
    res = dict[id]
    return res

dict = { '1': 'Ivan Petrov',
        '2': 'Fedor Sidorov',
        '3': 'Kate Ivanova'
    }

if __name__ == "__main__":
    app.run()