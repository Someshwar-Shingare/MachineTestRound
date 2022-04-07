'''
Database programing using flask_sqlalchemy:
1.pip install mysqlclient
2.pip install flask_sqlalchemy
'''
# Table creation
'''
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/batch10_30'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # to suppress the warning
db=SQLAlchemy(app=app)  # for binding flask application with ORM

class Employee(db.Model):
    eid = db.Column(db.Integer,primary_key = True)
    ename = db.Column(db.String(20))
    eaddr = db.Column(db.String(20))

@app.route('/')
def homeView():
    return 'Database starts!!'

if __name__=='__main__':
    db.create_all()
    app.run(debug=True)
'''



#insert static data into table
'''
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/batch10_30'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app=app)

class Employee(db.Model):
    eid = db.Column(db.Integer,primary_key = True)
    ename = db.Column(db.String(20))
    eaddr = db.Column(db.String(20))
    #ecity = db.Column(db.String(10))    #we cannot add column after table creation in flask

    def __str__(self):    #for printing the object on terminal 
        return f'{self.ename}'
@app.route('/')
def homeView():
    e = Employee(ename = 'Abc',eaddr = 'Pune')
    print(e)
    db.session.add(e)
    db.session.commit()
    return f'Inserted the record named {e.ename}'

if __name__=='__main__':
    db.create_all()      #to create table
    app.run(debug=True)
'''

#Insert data through form in database
'''
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/batch10_30'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app=app)

class Employee(db.Model):
    eid = db.Column(db.Integer,primary_key = True)
    ename = db.Column(db.String(20))
    eaddr = db.Column(db.String(20))
    #ecity = db.Column(db.String(10)) we cannot add column after table creation in flask

    def __str__(self):
        return f'{self.ename}'
@app.route('/')
def homeView():
    return render_template('register.html')

@app.route('/empreg',methods = ['GET','POST'])
def insertView():
    if request.method == 'POST':
        ename = request.form.get('ename')
        eaddr = request.form.get('eaddr')
        e = Employee(ename = ename,eaddr = eaddr)
        db.session.add(e)
        db.session.commit()
        return f'last record inserted is : {e.ename}'
    else:
        return render_template('register.html')

if __name__=='__main__':
    #db.create_all()
    app.run(debug=True)
'''

# Insert data through form in database and display the data
'''
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/batch10_30'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app=app)         # for binding flask application with ORM

class Employee(db.Model):
    eid = db.Column(db.Integer,primary_key = True)
    ename = db.Column(db.String(20))
    eaddr = db.Column(db.String(20))
    #ecity = db.Column(db.String(10)) we cannot add column after table creation in flask

    def __str__(self):
        return f'{self.ename}'
@app.route('/')
def homeView():
    obj =  Employee.query.all()       # to fetch full table data
    #obj = Employee.query.get(2)      # to fetch particular data with given eid
    return render_template('register.html',obj = obj)

@app.route('/empreg',methods = ['GET','POST'])
def insertView():
    if request.method == 'POST':
        ename = request.form.get('ename')
        eaddr = request.form.get('eaddr')
        e = Employee(ename = ename,eaddr = eaddr)
        db.session.add(e)
        db.session.commit()
        return f'last record inserted is : {e.ename}'
    else:
        return render_template('register.html')

if __name__=='__main__':
    #db.create_all()
    app.run(debug=True)
'''

#Update and Delete data
from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/batch10_30'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app=app)         # for binding flask application with ORM

class Employee(db.Model):
    eid = db.Column(db.Integer,primary_key = True)
    ename = db.Column(db.String(20))
    eaddr = db.Column(db.String(20))
    #ecity = db.Column(db.String(10)) we cannot add column after table creation in flask

    def __str__(self):
        return f'{self.ename}'
@app.route('/')
def homeView():
    obj =  Employee.query.all()       # to fetch full table data
    #obj = Employee.query.get(2)      # to fetch particular data with given eid
    return render_template('register.html',obj = obj)

@app.route('/empreg',methods = ['GET','POST'])
def insertView():
    if request.method == 'POST':
        ename = request.form.get('ename')
        eaddr = request.form.get('eaddr')
        e = Employee(ename = ename,eaddr = eaddr)
        db.session.add(e)
        db.session.commit()
        return f'last record inserted is : {e.ename}'
    else:
        return render_template('register.html')
@app.route('/update/<int:eid>',methods = ['GET','POST'])
def updateView(eid):
    obj = Employee.query.get(eid)
    print(obj)
    if request.method == 'POST':
        obj.ename = request.form.get('ename')
        obj.eaddr = request.form.get('eaddr')
        db.session.commit()
        return redirect(url_for('homeView'))
    return render_template('update.html',obj_key = obj)

@app.route('/delete/<int:emp_id>')
def deleteView(emp_id):
    e = Employee.query.get(emp_id)
    db.session.delete(e)
    db.session.commit()
    return redirect(url_for('homeView'))
if __name__=='__main__':
    #db.create_all()
    app.run(debug=True)
