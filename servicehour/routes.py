from servicehour import app
from flask import render_template, url_for, redirect
from servicehour.forms import InputForm

@app.route("/")
def redir():
    return redirect(url_for('index'))

@app.route("/index", methods=['GET','POST'])
def index():
    title = "Index"
    form = InputForm()
    return render_template('index.html', title=title, form=form)