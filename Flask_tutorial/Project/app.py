from flask import Flask,render_template, redirect, request, url_for
from flask.wrappers import Request
from flask_bootstrap import Bootstrap
# render_template : templates의 html 파일을 라우팅 하는데 필요하다.
app = Flask(__name__)
test = []
for i in range(1,10):
    for j in range(1,10):
        one = str(i)
        two = str(j)
        result = str(i*j)
        test.append(one+"x"+two+"="+result)
count = 0
@app.route("/gugudan")
def index():
    return render_template('gugudan.html',test=test, count=count) #변수값 넣어주기

"""
@app.route("/hello") #정적 라우팅 주소 지정
def hello():
    return 'hello'
"""
"""
@app.route('/<pagename>') #동적 라우팅 변수로 주소지정
def hello(pagename):
    return render_template(pagename)
"""

@app.route("/animal")
def animal():
    return render_template('animal.html')

@app.route("/dog")
def dog():
    return render_template('dog.html')
#==================================================
@app.route('/')
@app.route('/<int:num>')
def inputTest(num=None):
    return render_template('input_gugu.html',num=num)
#===============================================================
@app.route("/calculate",methods=['POST'])
def calculate(num=None):
    if request.method == 'POST':
        temp = request.form['num']
        if temp == '':
            return redirect(url_for('inputTest',num=None))
    else:
        temp = None
    return redirect(url_for('inputTest',num=temp))



if __name__ =='__main__':
    app.run(debug=True)

#debug = True 디버그 모드 허용으로 코드 변경시 재시작하지 않아도 새로고침을 하면 적용

