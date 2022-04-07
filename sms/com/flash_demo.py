#Flash messages by using flash() function
#1 Flash function without category
'''
from flask import Flask,render_template,flash
app=Flask(__name__)
app.secret_key='cjc123#'
@app.route('/')
def m1():
    flash('Flash messages 1')
    flash('Flash messages 2')
    flash('Flash messages 3')
    return render_template('final.html')

if __name__ =='__main__':
    app.run(debug=True)
'''

#2 Flash function with category
from flask import Flask,render_template,flash
app=Flask(__name__)
app.secret_key='cjc123#'
@app.route('/')
def m1():
    flash('Flash messages 1')
    flash('Flash messages 2')
    flash('Flash messages 3')
    return render_template('final.html')
@app.route('/cat')
def m2():
    flash('success message','success') #flash(message,category)
    flash('error message','error')
    flash('warning message','warning')
    return render_template('cat.html')

if __name__ =='__main__':
    app.run(debug=True)
