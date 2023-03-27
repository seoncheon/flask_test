from flask import Flask

'''
    create_app은 플라스크 내부에서 정의된 함수명(수정X)
    flask run을 수행하면 내부적으로 엔트리포인트 모듈에서 create_app()을 찾는다
    차후, 다른 모듈에서는 flask.current_app 이라는 변수로 app에 접근 가능
'''

def create_app():
    app = Flask(__name__)

    # 환경변수 초기화
    init_environment( app )
    # 블루프린트 초기화
    init_bluprint( app )

    return app

def init_environment(app):
    # 특정 파일( cfg, ... ) 등을 읽어서 처리 가능 
    app.config.from_pyfile( 'resource/config.cfg', silent=True )
    # py을 모듈 가져오기 해서 객체를 세팅해서 처리
    import service.config as config
    app.config.from_object( config )
    # 환경변수(OS레벨, 플라스크 레벨, 사용자정의 레벨 모두 포함) 모두 출력
    print('\n' + '-'*20)
    # 개별 환경 변수값 추출 : 딕셔너리와 동일한 방식으로 추출 가능 (get함수 활용)
    print(app.config.get('SECRET_KEY'))
    #for k, v in app.config.items():
    #    print(k, v)
    print('-'*20 + '\n')

def init_bluprint(app):
    # app에 블루프린트 객체를 등록한다
    
    # 블루프린트로 정의된 개별 페이지 관련 내용 로드 -> 로드하지 않으면 라우팅된 @main이 아무 작동하지 않음
    from .controllers import main_controller
    from .controllers import auth_controller

    # 이 위치에서는 service를 생략하고 표현 가능(controllers와 동일한 위치에 있기 때문)
    # from service.controllers import bp_main
    from .controllers import bp_main, bp_auth
    
    # 플라스크 객체에 블루프린트 등록
    app.register_blueprint(bp_main)
    # 실습 http://127.0.0.1:5000/auth/ 접속시 인증 홈이란 내용이 나오도록
    # auth 관련 블루프린트 구성
    app.register_blueprint(bp_auth)    