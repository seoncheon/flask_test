'''
    - POST 방식으로 데이터 전송하기
        - 클라이언트 ( Json / Xml / Text / Form ( 키=값&키=값&... )  / Form-encode / Graphql / Binary )
            - form 전송 : 사용자에게 입력을 받을 때 활용, 가입과 같은 형식일 경우 활용
                - Form / Form-encode 형식만 가능
                - <form action="http://127.0.0.1:5000/link" method="post"> # form 전송에서 가장 중요한 2가지 태그 action, method
                      <input name="name" value="hello"/>                   # 단독 태그는 마지막에 /로 닫아줌
                      <input name="age" value="100"/>
                      <input type="submit" value="전송"/>
                  </form>
            - ajax 전송 (jQuery로 표현) : 무게중심이 클라이언트 쪽에 있기 때문에 반드시 입력을 받아야 함
                - Json / Xml / Text / Form ( 키=값&키=값&... )  / Form-encode / Graphql / Binary 형식만 가능
                - $.post({
                    url  : "http://127.0.0.1:5000/link",
                    data : "name=hello&age=100",
                    success : (res)=>{},
                    error   : (err)=>{}
                  })
        - 서버
            - post 방식 데이터 추출
            - name = request.form.get('name')
            - age  = request.form.get('age')
    
    - /link 쪽으로 요청하는 방식은 다양할 수 있다. 단, 사이트 설계상 1가지로만 정의되어 있다면
      다른 방식의 접근은 모두 비정상적인 접근이다(웹 크롤링, 스크래핑, 해킹 등이 대상)
      이런 접근을 필터링할 것인가? 보안의 기본사항
'''
from d4 import select_login

from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

# @app.route() -> 기본적으로 GET 방식
# 메소드 추가는 method=['POST', ..]
@app.route('/')
def home():
    return 'HELLO'

@app.route('/login', methods=['POST', 'GET'])
def login():
    # 메소드별 분기
    if request.method == 'GET':
        return render_template('login.html')
    else: # POST
        # 1. 로그인 정보 회득
        uid = request.form.get('uid')
        upw = request.form.get('upw') # 암호는 차후에 암호화 해야 함 (관리자도 볼 수 없다 -> 일반적으로 해싱을 통해 원값을 모르게 함)
        print(uid, upw)
        # 2. 회원 여부 쿼리
        result = select_login(uid, upw)
        # 3. 회원이면
        if result:
            # 3-1. 세션 생성, 기타 필요한 조치 수행
            # 3-2. 서비스 메인 화면으로 이동
            pass
        # 4. 회원 아니면
        else:
            # 4-1. 적당한 메시지 후 다시 로그인 유도
            return render_template('error.html')
        # return redirect('https://www.naver.com') # redirect : 요청을 다른 URL로 포워딩

if __name__ == "__main__":
    app.run(debug=True)