from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def get_periplus():
    with open('sample_v2.json', 'r') as myfile:
        data = json.load(myfile)
    return render_template('index.html', datas=data)


if __name__ == '__main__':
    app.run(debug=True)