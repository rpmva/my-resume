from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/courses')
def show_all_courses():
    courses = [
        'ACCT208',
        'CISC250',
        'FINC311',
        'BUAD306',
        'BUAD470'
    ]
    return render_template('courses.html', courses=courses)

@app.route('/about')
def about():
    return render_template('about.html')
