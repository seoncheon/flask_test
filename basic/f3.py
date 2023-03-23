'''
    클라이언트가 서버에게 데이터를 보내는 방법
    - 방법 : method = GET, POST, PUT, ... <- http(or https) 프로토콜(통신규약, 서로 데이터를 주고받는 약속)에서 정의
        - http는 헤더(고정 크기)를 먼저 전송, 바디(가변 크기)를 나중에 전송
        - get 방식
            - 헤더만 전송 -> 고정크기만 전송 -> 보낼 양의 최대치가 정해져 있다 -> 소량만 보냄
            - http 헤더만 알면, 패킷(전송 데이터)를 가로채서 데이털르 해킹할 수 있다 -> 보안에 취약
        - post 방식
            - 헤더(바디의 크기가 세팅되어 있음) 전송 -> 바디 전송 -> 대량 전송 가능
            - 구조를 모르기 때문에 보안에 상대적으로 우수, 암호화 가능 -> 보안 양호 (상대적)
        - put 방식
            - DB에 데이터를 넣을 때 사용 (제한적 용도)
            - 회원가입과 같은 경우 활용됨
    - 방식
        - form 전송 : <form> 태그 사용, 화면이 껌뻑(순식간에 진행, x로 주소창 앞의 아이콘 변경)
        - ajax 전송 : 백그라운드로 서버와 통신, 화면은 고정
        - websocket : 웹소켓을 열어서 통신
        - 동적 파라미터 : get의 헤더를 활용하여 URL에 데이터를 넣어서 보내는 방식
    - 동적 파라미터
        - http 헤더의 주소 정보를 활용
'''
from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world"

# 동적 파라미터 활용 -> 문자열 타입으로 전송
# 용량은 헤더 사이즈, 주소 크기를 초과할 수 없다
# 파라미터는 함수 인자를 통해서 함수 내부로 진입
# #, <, >은 전달 안됨 / 한글, 특수, 영대, 영소 가능
# URL 인코딩으로 전달하면 모두 전달가능 %12%ae...
@app.route('/news/<news_id>')
def news(news_id):
    return "전달된 데이터 [ %s ]" % news_id

# URL을 무한대로 생산할 수 있다
# 1개 이상도 전달 가능한가? + 위치 조정
# http://~/전달값1/news2/전달값2
@app.route('/<news_id>/news2/<news_author>')
def news2(news_id, news_author):
    return "전달된 데이터 [ %s ] [ %s ]" % (news_id, news_author)

# 타입 제한이 가능한가? int, float, path
@app.route('/news3/<int:news_id>')
def news3(news_id):
    return "전달된 데이터 [ %s ]" % news_id

# path
# 전달값을 무한대로 늘려주는 옵션
# http://127.0.0.1:5000/news4/1/2/3/4/5/6/7/8/9/home/동국/10
@app.route('/news4/<path:news_id>')
def news4(news_id):
    # 정보를 구분해서 여러개로 전달 가능(가변적)
    return "전달된 데이터 [ %s ]" % news_id.split('/')[-2]

if __name__ == "__main__":
    app.run(debug=True)