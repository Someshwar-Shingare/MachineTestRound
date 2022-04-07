from flask import Flask
from com.Admin import admintest
from com.Client import clienttest
app = Flask(__name__)
app.register_blueprint(admintest.admin_bp)
app.register_blueprint(clienttest.client_bp)

@app.route('/')
def m1():
    return 'Welcome to Blueprint Demo'

if __name__=='__main__':
    app.run(debug=True)
