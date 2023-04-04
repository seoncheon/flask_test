# 풀링 기법 적용
import sqlalchemy.pool as pool
import pymysql
from flask import current_app

# 커넥션 풀을 관리하는 객체
db_pool = None

# 커넥션 처리하는 함수
def get_conn():
    c = pymysql.connect(host='localhost',
                        user='root',
                        password='rlalrlal3',
                        database='ml_db',
                        cursorclass=pymysql.cursors.DictCursor)
    return c

# 풀링 생성 함수
def init_pool():
    global db_pool
    '''
        pool_size : 현재 구성상 생성한 커넥션 수, 가장 작은값(최소 단위)
        max_overflow : 물리적으로 버틸수 있는 최대값으로 설정(최대 동시처리수)
    '''
    db_pool = pool.QueuePool(get_conn, max_overflow=10, pool_size=5)

# 로그인 처리
def login(uid, upw):
    row = None
    print('풀링에서 관리하는 커넥션 수 : ', db_pool.size())
    # 커넥션 풀에서 커넥션 1개를 빌려와서 쿼리 수행 -> 반납
    # 1. 커넥션 획득
    conn = db_pool.connect()
    # 2. 커서 획득
    with conn.cursor() as cur:
        sql = '''
            select
                *
            from
                users
            where
                uid=%s and upw=%s
        '''
        cur.execute( sql, (uid, upw) )
        # 3. 반납
        conn.close()
        row = cur.fetchone()
    return row