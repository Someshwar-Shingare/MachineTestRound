'''
from flask import Flask
app = Flask(__name__)
@app.route('/log')
def m1():
    return 'Hello'
@app.route('/log1',methods =['POST'])
def m2():
    return 'm2 function'
@app.route('/log2')
def m3():
    return 10/0
@app.errorhandler(404)
def error404(error):
    return 'please check your url!'
@app.errorhandler(405)
def error405(error):
    return 'please check your method type!'
@app.errorhandler(500)
def error500(error):    # 500 is used when we don't have any error status code,when we use it we should remove debug=True from run
    return 'Logical error'

if __name__=='__main__':
    app.run()
'''


# abort function for custom error handling
from flask import Flask,abort
app = Flask(__name__)
@app.route('/')
def m1():
    return 'Hello'
@app.route('/log/<uname>')
def m2(uname):
    if uname[0].isdigit():
        abort(404)    # use the error code which you have handled in your program
    return 'Correct username!'
@app.errorhandler(404)
def error404(error):   # function name can be anything but parameter should be 'error' only
    return 'please check your url!'
@app.errorhandler(405)
def error405(error):
    return 'please check your method type!'

if __name__=='__main__':
    app.run(debug=True)
