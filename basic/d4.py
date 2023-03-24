'''
    데이터베이스 접속 후 쿼리 수행 + 파라미터 전달
'''
import pymysql as my

def select_login(uid, upw):
    connection = None
    try:
        connection = my.connect(host        = 'localhost',  
                                port        = 3306,         
                                user        = 'root',       
                                password    = 'rlalrlal3', 
                                database    = 'ml_db',
                                # 조회 결과 : [ {}, {}, {}, ... ] 형태로 추출
                                cursorclass = my.cursors.DictCursor
                                )
        with connection.cursor() as cursor: 
            # 파라미터는 %s 표시로 순서대로 세팅된다, '값' -> ''는 자동으로 세팅된다
            sql = '''
                SELECT 
                    `uid`, `name`, regdate 
                FROM 
                    users 
                WHERE 
                    `uid` = %s 
                AND 
                    `upw` = %s;
            '''
            # execute() 함수의 2번 인자가 파라미터 전달하는 자리, 튜플로 표현
            cursor.execute(sql, (uid, upw))
            row = cursor.fetchone()
            print( row['name'] )
    except Exception as e:
        print('접속 오류', e)
    else:
        print('접속시 문제 없음')
    finally:
        if connection:
            connection.close()

# d4 개발자의 테스트 코드 -> 다른데서 땡겨쓸 때 호출되지 않도록(2번 수행되지 않도록) 하기 위함
if __name__ == "__main__":
    select_login('guest', '1234')