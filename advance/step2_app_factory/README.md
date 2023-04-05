# 어플리케이션 팩토리, 엔트리 위치 조정 및 코드 조정
    - 엔트리 위치 조정, 코드 조정
    - app = Flask(__name__)
        - 현재 이 코드는 전역 변수로 존재
        - 프로젝트 규모가 커지면, 순환참조를 할 확률이 크다
        - flask 구현시 어플리케이션 팩토리라는 형태로 사용하라고 권장

# 방법
    - 플라스크 객체를 생성하는 코드, 특정 패키지 밑에 위치
        - 특정 패키지 밑에 위치 -> ex) service
        - __init__.py 로 이름 변경
        - 구조
            service
            L __init__.py
        - 최종 실행 명령
            - flask --app service --debug run

# 블루 프린트
    - URL과 함수의 매핑(라우트)을 관리하는 도구

# 부트스트랩 <-> 머터리얼(안드로이드 스타일), ...
    - 부트스트랩 적용, 베이스 페이지 구성
        - https://getbootstrap.kr/docs/5.2/getting-started/download/
            - 다운로드 클릭 -> 압축 해제
            - static 폴더 하위에 파일 위치
                - bootstrap.min.css(or js)
            - https://getbootstrap.kr/docs/5.2/examples/
                - 다양한 UI 형태 예시로 제공

    - 디자인 적용 기준 설정
        - static 밑에 공통으로 사용할 CSS(부트스트랩) 적용
            - SaaS를 사용하는 회사도 존재 > CSS -> SaaS로 넘어가는 추세
    - flask-bootstrap -> 2017년 이후로 업데이트 X
        - 부트스트랩 버전 3.x -> 사용안함

# 입력폼 유효성 검사 및 비정상적인 루트로 접근시 처리 방지
    - 웹 프로그램에서 폼(FORM)은 사용자에게 입력 양식을 편리하게 제공
    - 폼 모듈을 활용하여 데이터 입력 필수여부, 길이, 형식, 유효성, 컨트롤 가능
    - flask-wtf
        - pip install Flask-WTF
        - 기본 구성
            - SECRET_KEY 필요
            - CSRF(Cross-Site Request Fogery)라는 웹 사이트 취약점 공격을 방지할 때 사용
            - CSRF는 사용자의 요청을 위조하여 웹 사이트를 공격하는 기법
            - CSRF 토큰을 웹페이지가 내려갈 때 삽입해서, 요청이 들어올 때 그 값이 요청을 타고 같이 들어오게 처리
                - 이 값이 요청에 존재하는 경우(값 자체도 유효해야함) 정상적인 루트로 진입했음을 인지한다
                - <input type='hidden' name='' value=''> 이 패턴을 잘 체크
                - SECRET_KEY 값을 기반으로 해싱해서 토큰을 생성함
                    - 웹 상에서 가장 잘 지켜야할 정보 -> SECRET_KEY를 잘 관리해야 함
    
    - 실습
        - 환경설정(변수)를 세팅해서 SECRET_KEY를 관리
        - 방식
            - OS 레벨에서 설정
            - 파이썬 객체로 설정 (o)
            - 환경변수 파일로 설정
                - 플라스크 객체가 로드하면서 세팅 (o)
                - 플라스크를 가동하면서 세팅
                - 키값, 디비연결값 등 외부에서 엑세스하여 컨트롤할 수 있는 값들은 뜯어내어 환경변수로 저장
        - 질문폼 페이지 생성
            - url : ~/main/question, get
            - html : question.html
                - base.html를 상속받아서 내부는 비워둔다

# JWT 개요
    - JSON Web Tokens
    - 토큰 기반 인증 방식
    - 왜 나왔고, 기존 대비 어떤 점이 유리한지는 2단계 기술시 표현
    - 세션에 고객 정보를 담아서 보관하지 않고, 고객의 필요한 정보를 토큰에 저장해서 클라이언트가 보관
      (고급으로 가면 방식에 따라서는 서버측에도 DB 보관), 이를 증명서로 활용한다 = 요청이 왔을 때 권한이 있는지 점검
    - 구성
        - header    : 헤더 -> jwt 토큰 유형, 해시 알고리즘 사용 정보 기록(RSA, SHA256, ...)
        - payload   : 저장할 정보 -> 클라이언트 정보, Meta data, ...
        - signature : 서명, 헤더에서 지정한 알고리즘으로 + 플라스크의 시크릿키를 재료로 서명을 생성(체크섬 용도)
    - 위험 요소
        - 해커는 서버측의 시크릿 키를 탈취하면, jwt 정보를 해킹할 수 있다.
        - 인증서의 시간이 길면(만료 시간) 해독의 확률이 높아진다 
            -> 기한을 짧게 구성 -> 사용자는 빈번하게 로그인 -> 불편함 + 오버헤드(서버측)
                -> 만료시간 연장 전략 혹은 리플래시 토큰을 서버측에 저장해서 이를 기반으로 토큰 기간을 갱신하는 전략 = 2단계에서 진행
    - 설치
        - pip install PyJWT bcrypt

# TODO 주석 활용
    - TODO: 내용
        - 해야할 작업
    - FIXME: 내용
        - 오작동, 버그가 발생되는 코드
    - HACK: 내용
        - 해결은 했으나, 깔끔하지 않은 경우(개선의 여지)
    - XXX: 내용
        - 이 부분은 큰 문제점, 오류를 가지고 있다

# 데이터베이스 연동
    - pool (풀링 기법)
        - 백엔드 서버가 가동하면, 백엔드와 데이터베이스간 일정량의 커넥션을 미리 맺은 후
        - 큐(Queue : 먼저 들어간 데이터가 먼저 나온다) 구조에 담아서 관리
        - 접속과 해제라는 반복 작업에 따른 응답시간 지연 원인을 제거, 일정량의 동접이 발생했을 때, 안정적인 처리속도 제공
        - sqlalchemy
    - ORM 방식
        - 객체 지향 방식으로 코드에서 데이터베이스 연동, 데이터 처리 등을 코드레벨에서 관리
        - 원칙적으로는 SQL을 몰라도 처리 가능
            - 데이터베이스 벤더가 교체되더라도 동일하게 작동
        - 단점
            - 쿼리가 최적화되었다고 볼 수 없다(기계적 생성)
        - flask-migrate, sqlalchemy
    - 설치
        - pip install sqlalchemy flask-migrate
    - 코드 작성
        ```
        from flask_sqlalchemy import SQLAlchemy
        from flask_migrate import Migrate

        db = SQLAlchemy()
        migrate = Migrate()

        db.init_app(app)
        migrate.init_app(app)
        < service의 __init__.py >

        ---------------------------------------------
     
        # ORM 처리를 위한 환경변수 설정 (임의 설정)
        DB_PROTOCOL = "mysql+pymysql"
        DB_USER     = "root"
        DB_PASSWORD = "rlalrlal3"
        DB_HOST     = "127.0.0.1"
        DB_PORT     = 3306
        DB_DATABASE = "my_db" # 새로 만들, 이 서비스에서 사용한 데이터베이스명

        # 이 환경변수는 migrate가 필수로 요구하는 환경변수
        SQLALCHEMY_DATABASE_URI=f"{DB_PROTOCOL}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
        # sqlalchemy modify 비활성 ( SQLALCHEMY_DATABASE_URI와 세트로 사용 )
        SQLALCHEMY_TRACK_MODIFICATIONS=False
        < config의 __init__.py >
        ```

        - 데이터베이스 생성, 초기화
            - --app service 은 없어도 되는데, 이 앱은 app or wsfi로 시작하는 엔트리가 없어서 별도로 지정해야 한다
            - flask --app service db init
                - sqlite : 소형 데이터베이스, 스마트폰에 사용하는 DB. 이 경우에는 데이터베이스 생성을 자동으로 해준다
                           파일럿 형태에서 사용
                - mysql 같은 데이터베이스(케이스별로 상이)는 실제로는 생성 안됨
            - 이를 실행하면 migrations 폴더가 생긴다 (내부는 자동으로 만들어지는 구조 -> 관여하지 않는다)
                - 단, versions 밑으로 수정할 때마다 새로운 버전의 DB 관련 파일이 생성된다

        - 모델(테이블) 생성, 변경
            - model > models.py에 테이블 관련 내용 기술
            - service > __init__.py
                - from .model import models : 주석 해제 or 신규 작성
            - flask --app service db migrate
            +-----------------+
            | Tables_in_my_db |
            +-----------------+
            | alembic_version |
            +-----------------+
            1 row in set (0.001 sec)

        - 모델(테이블) 생성, 변경 후 데이터베이스에 적용 : 일종의 커밋
            - flask --app service db upgrade
            +-----------------+
            | Tables_in_my_db |
            +-----------------+
            | alembic_version |
            | answer          |
            | question        |
            +-----------------+

        - 컨테이너 이미지 생성시
            - 위의 명령들 3개를 차례대로 수행해서 데이터베이스 초기화 및 생성과정을 수행

    - 필요한 기능들 시뮬레이션
        - DBA는 SQL문을 작성해서 쿼리 구현
        - ORM에서는 shell을 열어서 파이썬 코드로 구현
        - flask --app service shell
            - 질문 등록
            - 질문 조회
            - 답변 등록
                ...
            ```
            >>> from service.model.models import Question, Answer 
            >>> from datetime import datetime
            >>> from service import db

            >>> q1 = Question(title="질문1", content="내용1", reg_date=datetime.now())
            >>> db.session.add(q1)
            >>> db.session.commit()
            < table에 데이터 밀어넣기 >
            ```