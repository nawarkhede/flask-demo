from flask import Flask, url_for, request, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World'


@app.route('/profile/<profile_id>')
def profile(profile_id):
    return 'Hello %s' % (profile_id)


@app.route('/show')
def show():
    print url_for('profile', profile_id='nawarkhede')
    return 'view console'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return 'via get'
    if request.method == 'POST':
        return 'via post'
    return 'this is never gonna happen'


@app.route('/html')
def html():
    return render_template('index.html', name='nawarkhede')
