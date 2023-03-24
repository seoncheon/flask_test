from flask import Flask, render_template, url_for, session, redirect, request
from d4 import select_login

app = Flask(__name__)
app.secret_key = 'asdkfjaksiou'

@app.route('/')
def home():
    if not 'uid' in session:
        return redirect(url_for('login'))
    return 'HELLO WORLD'

# 메소드 받기
@app.route('/login', methods=['POST', 'GET'])
def login():
    # 메소드별 분기
    if request.method == 'GET':
        return render_template('login.html')
    else:   
        # 로그인 id와 pw를 받고
        uid = request.form.get('uid')
        upw = request.form.get('upw')
        # 로그인 성공 여부
        result = select_login(uid, upw)
        if result:
            session['uid'] = uid
            return redirect(url_for('home'))
        else:
            return render_template('error.html', msg='로그인실패')

if __name__ == '__main__':
    app.run(debug=True)
