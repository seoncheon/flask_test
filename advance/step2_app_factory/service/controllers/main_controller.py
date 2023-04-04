'''
    메인 서비스를 구축하는 컨트롤러
    - 라우트 : URL과 이를 처리할 함수 연계
    - 비즈니스 로직 : 사용자가 요청하는 주 내용을 처리하는 곳
'''

from flask import render_template, request, redirect, url_for, Response
# 엔트리포인트가 step2_app_factory이므로 그 아래의 service.controller의 __init__.py에서 bp_main을 들고온다
from service.controllers import bp_main as main
from service.forms import FormQuestion
# 환경변수 시크릿키 획득을 위해서 Flask 객체 획득
from flask import current_app
import jwt
from datetime import datetime
import time

# 127.0.0.1/main/
@main.route('/')
def home():
    # 1. 쿠키 중에 토큰 획득 -> 실패 -> 401(권한없음)
    token = request.cookies.get('token')
    SECRET_KEY = current_app.config['SECRET_KEY']
    print(token, SECRET_KEY)
    if not token or not SECRET_KEY:
        return Response(status=401)
    
    try:
        # 2. 디코딩 -> 실패하면 -> 401
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        # 3. 유효 날짜 추출, 현재 시간 기준보다 과거인지 체크 -> 과거라면 : 만료 -> 401
        if payload['exp'] < time.mktime(datetime.utcnow().timetuple()): # 현재 시간보다 과거 = 만료
            return Response(status=401)
        return render_template('index.html')
    # 토큰이 유효하지 않거나
    except jwt.InvalidTokenError:
        return Response(status=401)
    # 인증이 만료되었거나
    except jwt.ExpiredSignatureError:
        return Response(status=401)
    # 디코딩이 실패 -> 토큰이 손상된 경우
    except jwt.exceptions.DecodeError:
        return Response(status=401)

# # 127.0.0.1/main/question 
@main.route('/question', methods=['GET', 'POST'])
def question():
    form = FormQuestion()
    # post 방식으로 전송되고 유효성 검사도 통과한 경우
    if request.method == 'POST' and form.validate_on_submit():
        return redirect(url_for('main_bp.home'))
    return render_template('question.html', wtf=form)
