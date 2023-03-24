import pymysql as my

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
    with connection.cursor() as cursor: # cursor는 with문을 벗어나면 자동으로 닫힘
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
        cursor.execute(sql)
        row = cursor.fetchone()
        # 1. 결과 확인 -> 딕셔너리 -> 이름만 추출하시오 -> ['게스트']
        print( row['name'] )
        pass
except Exception as e:
    print('접속 오류', e)

else:
    print('접속시 문제 없음')

finally:
    if connection:
        connection.close()