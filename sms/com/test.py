from flask import Flask
app=Flask(__name__)
@app.route('/')
def m1():
    print('Hello')
    return 'Welcome to Flask!! HELLO WORLD'

@app.route('/log')
def m2():
    return 'Hello from m2 function'
if __name__ =='__main__':
    app.run(debug=True)
