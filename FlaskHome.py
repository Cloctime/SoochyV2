from flask import Flask,render_template,request
app = Flask(__name__)


@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        titre=request.form['titre']
        return render_template("page2.html",result =titre)

    return render_template('home.html')
