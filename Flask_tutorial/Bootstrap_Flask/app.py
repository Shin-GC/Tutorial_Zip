from flask import Flask,render_template 
from flask_bootstrap import Bootstrap

 
app = Flask(__name__,template_folder='templates')
Bootstrap(app) 
print(__name__)
@app.route('/')
def index_page(): 
    return render_template('index.html') 

if __name__ =='__main__' :
    app.run(debug=True) 