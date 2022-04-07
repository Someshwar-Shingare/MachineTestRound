#Hidden Form Field
'''
from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def m1():
    return render_template('first.html')

@app.route('/first')
def m2():
    return render_template('second.html')
@app.route('/second')
def m3():
    return render_template('third.html')

@app.route('/third')
def m4():
    return render_template('display.html')

if __name__ =='__main__':
    app.run(debug=True)
'''

#Cookies
'''
from flask import Flask,render_template,request,make_response
app=Flask(__name__)
@app.route('/')
def m1():
    return render_template('first.html')

@app.route('/first')
def m2():
    res = make_response(render_template('second.html'))
    res.set_cookie('fd',request.args.get('d1')) #set cookie( key, value, max_age)
    return res
@app.route('/second')
def m3():
    res = make_response(render_template('third.html'))
    res.set_cookie('sd', request.args.get('d2'))
    return res

@app.route('/third')
def m4():
    res = make_response(render_template('display.html'))
    res.set_cookie('td', request.args.get('d3'))
    return res

if __name__ =='__main__':
    app.run(debug=True)
'''

'''
#cookie max age
from flask import Flask,render_template,request,make_response
app=Flask(__name__)
@app.route('/')
def m1():
    return render_template('first.html')

@app.route('/first')
def m2():
    res = make_response(render_template('second.html'))
    res.set_cookie('fd',request.args.get('d1'),max_age=60*60*24*365*2)
    return res
@app.route('/second')
def m3():
    res = make_response(render_template('third.html'))
    res.set_cookie('sd', request.args.get('d2'))
    return res

@app.route('/third')
def m4():
    res = make_response(render_template('display.html'))
    res.set_cookie('td', request.args.get('d3'))
    res.set_cookie('fd', request.cookies.get('fd'),max_age=0)
    return res

if __name__ =='__main__':
    app.run(debug=True)
'''

#SESSION
from flask import Flask,render_template,request,session
app=Flask(__name__)
app.secret_key='cjc123#'
@app.route('/')
def m1():

    return render_template('first.html')

@app.route('/first')
def m2():
    session['fd'] = request.args.get('d1')
    return render_template('second.html')
@app.route('/second')
def m3():
    session['sd'] = request.args.get('d2')
    return render_template('third.html')

@app.route('/third')
def m4():
    session['td'] = request.args.get('d3')
    return render_template('display.html')

if __name__ =='__main__':
    app.run(debug=True)
