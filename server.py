from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)
app.secret_key = 'secreto'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['place'] = request.form['place']
        session['programming_language'] = request.form['programming_language']
        session['comments'] = request.form['comments']
        return redirect(url_for('result'))
    return render_template('index.html')

@app.route('/result')
def result():
    name = session.get('name')
    place = session.get('place')
    programming_language = session.get('programming_language')
    comments = session.get('comments')
    return render_template('resultado.html', name=name, place=place, programming_language=programming_language, comments=comments)

@app.route("/regresar")
def regresar():
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True, port= 5002)