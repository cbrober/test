from flask import Blueprint, render_template, request

admin=Blueprint('admin', __name__)
@admin.route('/', methods=['POST', 'GET'])
def admin_home():
    if request.method== 'POST':
        username=request.form.get('username')
        print(f"hello {username}")
        statement=f"hello {username}"
    return render_template('admin-home.html')
@admin.route('/fun')
def admin_fun():
    return render_template('fun.html')
