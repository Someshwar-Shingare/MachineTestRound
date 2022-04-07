'''
Flask Authentication:
1. pip install mysqlclient
2. pip install flask-sqlalchemy
3. pip install flask-login
'''
from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin,login_user,LoginManager,login_required,logout_user,current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/batch10_30'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'cjc123#'
db = SQLAlchemy(app=app)         # for binding flask application with ORM


login_manager = LoginManager()
login_manager.init_app(app)      #cofigure application to login
login_manager.login_view = 'loginView'  #name of your login view


class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(20),nullable = False)
    password = db.Column(db.String(20),nullable = False)
    #ecity = db.Column(db.String(10)) we cannot add column after table creation in flask

    def __str__(self):
        return f'{self.ename}'
@app.route('/')
def homeView():

    return render_template('home.html')
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id = user_id).first()


@app.route('/login',methods = ['GET','POST'])
def loginView():
    if request.method == 'POST':
        user = User.query.filter_by(username = request.form.get('unm')).first()
        if user:   #for handling the session and login things
            login_user(user)
            return redirect(url_for('finalView'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def registerView():
    if request.method == 'POST':
        unm = request.form.get('unm')
        pwd = request.form.get('pwd')
        new_user = User(username = unm,password = pwd)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('loginView'))
    return render_template('register.html')
@app.route('/logout')
@login_required
def logoutView():
    logout_user()
    return redirect(url_for('loginView'))

@app.route('/final', methods = ['GET','POST'])
@login_required
def finalView():
        return render_template('final.html')
if __name__=='__main__':
    db.create_all()
    app.run(debug=True)
