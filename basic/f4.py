'''
    - GET 방식으로 데이터 전송하기
        - 클라이언트
            - 링크 : 키=값 & 키=값, 단순히 보여줄 수만 있음
                - <a href="http://127.0.0.1:5000/link?name=hello&age=100">링크</a>
            - form 전송 : 사용자에게 입력을 받을 때 활용, 가입과 같은 형식일 경우 활용
                - <form action="http://127.0.0.1:5000/link" method="get">  <- form 전송에서 가장 중요한 2가지 태그 action, method
                      <input name="name" value="hello"/>                   <- 단독 태그는 마지막에 /로 닫아줌
                      <input name="age" value="100"/>
                      <input type="submit" value="전송"/>
                  </form>
            - ajax 전송 (jQuery로 표현) : 무게중심이 클라이언트 쪽에 있기 때문에 반드시 입력을 받아야 함
                - $.get({
                    url  : "http://127.0.0.1:5000/link",
                    data : "name=hello&age=100",
                    success : (res)=>{},
                    error   : (err)=>{}
                  })
        - 서버
            - get 방식 데이터 추출
            - name = request.args.get('name')
            - age  = request.args.get('age')
    
    - /link 쪽으로 요청하는 방식은 다양할 수 있다. 단, 사이트 설계상 1가지로만 정의되어 있다면
      다른 방식의 접근은 모두 비정상적인 접근이다(웹 크롤링, 스크래핑, 해킹 등이 대상)
      이런 접근을 필터링할 것인가? 보안의 기본사항
'''
from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

@app.route('/link')
def link():
    # request.args['name']과 같이 인덱싱하는 방식으로 데이터를 받는 경우
    # 데이터 누락시 서버가 셧다운됨 => 절대 사용하면 안됨
    # request.args.get('name') -> 데이터 누락시 None으로 나옴
    name = request.args.get('name') 
    age  = request.args.get('age')
    return "[%s] [%s]" % (name, age)

@app.route('/test')
def test():
    # 엔트리포인트(진입로, 프로그램 시작점)과 같은 경로에 templates/test.html 생성
    return render_template('test.html')

if __name__ == "__main__":
    app.run(debug=True)