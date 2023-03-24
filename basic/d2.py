'''
    데이터베이스 접속 후 쿼리 수행
'''
import pymysql as my

connection = None
try:
    connection = my.connect(host        = 'localhost',  
                            port        = 3306,         
                            user        = 'root',       
                            password    = 'rlalrlal3', 
                            database    = 'ml_db',
                            # 조회 결과 : [ {}, {}, {}, ... ] 형태로 추출
                            # 사용 안하면 [ (, ), (, ), ... ] 이런 형태로 나옴
                            #cursorclass = my.cursors.DictCursor
                            )
    # 쿼리 수행
    # pymysql은 커서를 획득해서 쿼리를 수행한다 -> Rule
    # 1. 커서 획득, 아무 것도 주지 않을 경우 기본형은 튜플
    # connection.cursor(my.cursors.DictCursors)
    with connection.cursor() as cursor:
        # 2. SQL문 준비
        sql = '''
            SELECT 
                `uid`, `name`, regdate 
            FROM 
                users 
            WHERE 
                `uid` = 'guest' 
            AND 
                `upw` = '1234';
              '''
        # 3. SQL 쿼리 수행
        cursor.execute(sql)
        # 4. 결과를 획득
        row = cursor.fetchone()
        # 5. 결과 확인 -> 이름만 추출하시오 -> '게스트'
        # 튜플로 결과를 받는 것은 결과값의 순서가 바뀌지 않는다는 전제하에 가능
        # 유연하게 대체하고 싶다면 컬럼순서 변경되던, 쿼리문의 순서가 변경 되던지 관계없이 대응
        # 순서없는 자료구조 -> 딕셔너리!!
        name = row[1]
        print( name )
        pass
except Exception as e:
    print('접속 오류', e)

else:
    print('접속시 문제 없음')

finally:
    if connection:
        connection.close()