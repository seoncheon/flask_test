SECRET_KEY = 'invisible' # 서비스시 추론이 불가한 해시값 추천
# 클래스를 정의해서 내부에 멤버로 표현해도 됨

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