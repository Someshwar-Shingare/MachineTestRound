from flask import Blueprint,render_template

client_bp= Blueprint('client',__name__,template_folder='templates')

@client_bp.route('/client')
def m1():
    return render_template('client.html')