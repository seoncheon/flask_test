from flask import render_template, request, url_for
from service.controllers import bp_auth as auth

# 127.0.0.1/auth/
@auth.route('/')
def home():
    # url_for( 별칭.함수명 ) -> url이 리턴
    # print(url_for('auth_bp.login'))
    return 'auth home'

@auth.route('/logi')
def login():
    return 'auth login'

@auth.route('/logout')
def logout():
    return 'auth logout'

@auth.route('/signup')
def signup():
    return 'auth signup'

@auth.route('/delete')
def delete():
    return 'auth delete'