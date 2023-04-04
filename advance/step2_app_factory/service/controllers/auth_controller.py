from flask import render_template, request, url_for, jsonify
from service.controllers import bp_auth as auth
# 시간 정보 획득, 시간차 계싼 함수
from datetime import datetime, timedelta
# Flask 객체 획득
from flask import current_app
import jwt, bcrypt

# 127.0.0.1/auth/
@auth.route('/')
def home():
    # url_for( 별칭.함수명 ) -> url이 리턴
    # print(url_for('auth_bp.login'))
    return 'auth home'

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # jwt관련 체크 -> 정상 or 오류(권한없음 = 401 error)
        # 1. uid, upw 획득
        uid = request.form.get('uid')
        upw = request.form.get('upw')
        # 2. uid, upw로 회원이 존재하는지 체크 -> 원래는 DB, 임시로 값비교
        if uid == 'guest' and upw == '1234':
            # 3. 회원이면 토큰 생성 (규격, 만료시간, 암호알고리즘 지정)
            payload = {
                # 저장할 정보는 알아서 구성 (고객정보가 기반)
                'id':uid,
                # 만료시간
                # 토큰이 발급되고 나서 24시간 후에 토큰은 만료된다
                'exp':datetime.utcnow()+timedelta(seconds=60*60*24)
            }
            # 토큰 발급 -> 시크릿키, 해시 알고리즘(HS256), 데이터(payload) 
            SECRET_KEY = current_app.config['SECRET_KEY'] # 환경변수값 획득
            # 발급
            token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
            # 4. 응답 전문 구성 -> 응답
            return jsonify( {'code':1, 'token':token} )

@auth.route('/logout')
def logout():
    return 'auth logout'

@auth.route('/signup')
def signup():
    # TODO : 비밀번호 암호화
    password = '1234'
    # 암호화된 값은 DB의 패스워드 컬럼에 저장
    b = bcrypt.hashpw( password.encode('utf-8'), bcrypt.gensalt() )
    # 확인 및 복호화
    # bcrypt.checkpw() -> 이것으로 암호가 일치하는지만 체크해서 로그인시 활용
    print( password, b, bcrypt.checkpw(password.encode('utf-8'), b) )
    return 'auth signup'

@auth.route('/delete')
def delete():
    return 'auth delete'