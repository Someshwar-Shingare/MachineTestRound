#GET request
'''
from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def m1():
    return render_template('login.html')

@app.route('/log')
def m2():
    uname=request.args.get('unm')
    password=request.args.get('pwd')
    print('username:',uname)
    print('password:',password)
    return render_template('success.html')
if __name__ =='__main__':
    app.run(debug=True)
'''

'''
#POST request

from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def m1():
    return render_template('login.html')

@app.route('/log',methods=['POST'])
def m2():
    uname=request.form.get('unm')
    password=request.form.get('pwd')
    print('username:',uname)
    print('password:',password)
    return render_template('success.html')
if __name__ =='__main__':
    app.run(debug=True)
'''

#Backend data to frontend using jinja tags
'''
{{ }} expression tag
{% %} code block
'''

from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def m1():
    return render_template('login.html')

@app.route('/log',methods=['POST'])
def m2():
    uname=request.form.get('unm')
    password=request.form.get('pwd')
    print('username:',uname)
    print('password:',password)
    return render_template('success.html',uname=uname,password=password,name='Guest')
if __name__ =='__main__':
    app.run(debug=True)
