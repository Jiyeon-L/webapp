from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/hello')
def hellohtml():
    return render_template("hello.html")

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        num = request.args["num"]
        name = request.args.get("name")
        return "GET으로 전달된 데이터({}, {})".format(num, name)
    else:
        num = request.form["num"]
        name = request.form["name"]
        return "POST로 전달된 데이터({}, {})".format(num, name)

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/gonaver', methods=['GET', 'POST'])
def gonaver():
    if request.method == 'GET':
        search = request.args["search"]
        return "{} 를(을) 검색하셨습니다".format(search)
    else:
        search = request.form["search"]
        return "{} 를(을) 검색하셨습니다".format(search)

if __name__ == '__main__':
    app.run()
