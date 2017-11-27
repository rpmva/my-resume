from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/courses')
def show_all_courses():
    courses = [
        ['ACCT208','Introduction to managerial accounting','Topics: manufacturing accounting, cost-volume-profit analysis, job-order accounting, budgeting, standard costs and variance analysis, contribution approach to decision analysis, absorption and variable costing.'],
        ['CISC250','Business Telecommunication Networks','Examines technologies of information transmission currently utilized in the business environments and the implications of these technologies upon the development and implementation of information systems.'],
        ['FINC311','Principles of Finance','Introduces fundamental techniques and concepts related to the financial management of business firms.'],
        ['BUAD306', 'Introduction to Service and Operations Management','Analysis of major problems faced by operations managers at different levels of management.'],
        ['BUAD470','Sales Management and Selling','Selling as the process of commercial persuasion and as a service to the customer.']
        ]

    return render_template('courses.html', courses=courses)

@app.route('/about')
def about():
    return render_template('about.html')
