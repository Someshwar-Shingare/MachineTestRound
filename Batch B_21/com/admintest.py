from flask import Blueprint,render_template

admin_bp = Blueprint('admin',__name__,template_folder='templates')
'''
Blueprint(1,2,3)
1. It is Blueprint name used by flask routing system
2. Blueprint's import name which is used to locate blueprint resources
3. Template directory name

'''
@admin_bp.route('/admin')
def m1():
    return render_template('admin.html')