from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def m1():
    print('Hello')
    return '''
    <html>
    <head></head>
    <body>
    <h1>This is HTML page</h1>
    </body>
    </html>
    '''
@app.route('/log')
def m2():
    return render_template('success.html')
if __name__ =='__main__':
    app.run(debug=True)