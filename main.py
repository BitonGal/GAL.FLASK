from flask import Flask, redirect, url_for
app = Flask(_name_)


@app.route('/')
def main():
    return 'Welcome to the best website!'

@app.route('/about')
def about():
    return 'Welcome About page '

@app.route('/page')
def page():
 return redirect('/')

@app.route('/anotherPage')
def anotherPage():
 return redirect(url_for('about'))


if _name_ == '_main_':
    app.run()
