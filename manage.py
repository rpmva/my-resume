from flask_script import Manager
from my_resume import app, db, Professor, Course

manager = Manager(app)


@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    c1 = Course(course_number ='ACCT208', title ='Introduction to managerial accounting', description = 'Topics: manufacturing accounting, cost-volume-profit analysis, job-order accounting, budgeting, standard costs and variance analysis, contribution approach to decision analysis, absorption and variable costing.')
    c2 = Course(course_number = 'CISC250', title ='Business Telecommunication Networks', description = 'Examines technologies of information transmission currently utilized in the business environments and the implications of these technologies upon the development and implementation of information systems.')
    c3 = Course(course_number = 'FINC311', title ='Principles of Finance', description = 'Introduces fundamental techniques and concepts related to the financial management of business firms.')
    c4 = Course(course_number = 'BUAD306', title ='Introduction to Service and Operations Management',description ='Analysis of major problems faced by operations managers at different levels of management.')
    c5 = Course(course_number = 'BUAD470', title ='Sales Management and Selling',description ='Selling as the process of commercial persuasion and as a service to the customer.')
    p1 = Professor(name="Michael G. Van Leer", department = "Accounting")
    p2 = Professor(name="Jinwei Cao", department = "Computer and Information Sciences")
    p3 = Professor(name="Christopher Michael Lynch", department = "Finance")
    p4 = Professor(name="Susan B. Murphy", department = "Business Administration")
    p5 = Professor(name="Sandra M. Fields", department = "Business Administration")
    db.session.add(c1)
    db.session.add(c2)
    db.session.add(c3)
    db.session.add(c4)
    db.session.add(c5)
    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    db.session.add(p4)
    db.session.add(p5)
    db.session.commit()
    

if __name__ == "__main__":
    manager.run()
