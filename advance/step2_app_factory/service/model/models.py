from service import db, migrate

# 테이블별로 클래스 설계
# 클래스        = 테이블
# 클래스 멤버   = 테이블 컬럼
# 클래스 객체   = 테이블의 row 데이터

# 질문 테이블
class Question(db.Model):
    pass

# 답변 테이블
class Answer(db.Model):
    pass