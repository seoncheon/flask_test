'''
    파이썬 <-> 데이터베이스
    파이썬으로 데이터베이스를 엑세스하여 쿼리를 전송, 수행결과를 받아오는 방식
        - SQL 수행
            - basic에서 수행
            - pymysql 패키지 사용
        - ORM 수행
            - advance에서 수행
    업무 포지션은 지원팀, 공용 API를 만드는 파트 -> 함수, 클래스 형태로 라이브러리 제공
    사용 방법에 대한 예제까지 제공

    1. 데이터베이스를 터미널을 통해 접속 -> root 권한으로 mysql에 접속
        $ mysql -u root -p
        Enter Password:
        MariaDB[(none)]>
    2. 데이터베이스 생성
        create database ml_db;
    3. 데이터베이스 목록 출력
        show databases;
        +--------------------+
        | Database           |
        +--------------------+
        | exchange_data_db   |
        | information_schema |
        | ml_db              |
        | mysql              |
        | news_data_db       |
        | performance_schema |
        | sys                |
        +--------------------+
    4. 현재 작업(사용)할 데이터베이스 지정
        use ml_db;
        MariaDB [ml_db]> show tables;
    5. 고객 테이블 생성
        # USING BTREE : 검색 속도를 높이는 방식 중에 하나로 특정 컬럼을 지정
        CREATE TABLE `users` (
            `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '고객 고유 관리 ID',
            `uid` VARCHAR(32) NOT NULL COMMENT '고객의 로그인 ID' COLLATE 'utf8mb4_general_ci',
            `upw` VARCHAR(128) NOT NULL COMMENT '고객 로그인 비번' COLLATE 'utf8mb4_general_ci',
            `name` VARCHAR(32) NOT NULL COMMENT '고객 이름' COLLATE 'utf8mb4_general_ci',
            `regdate` TIMESTAMP NOT NULL COMMENT '고객 가입일',
            PRIMARY KEY (`id`) USING BTREE,
            UNIQUE INDEX `uid` (`uid`) USING BTREE
        )
        COMMENT='고객 테이블'
        COLLATE='utf8mb4_general_ci'
        ENGINE=InnoDB
        ;

        # 컬럼 추가 : ADD COLUMN
        # 컬럼 변경 : MODIFY COLUMN
        # 컬럼 이름 포함 변경 : CHANGE COLUMN
        # 컬럼 삭제 : DROP COLUMN
        # 테이블 이름 변경 : RENAME
        # ALTER TABLE <테이블명> CHANGE COLUMN <OLD컬럼> <NEW 컬럼> <데이터 타입> [FIRST|AFTER <컬럼명>]

        ALTER TABLE `users`
        CHANGE COLUMN `upw` `upw` VARCHAR(128) NOT NULL COMMENT '고객 로그인 비번' COLLATE 'utf8mb4_general_ci' AFTER `uid`,
        CHANGE COLUMN `name` `name` VARCHAR(32) NULL DEFAULT NULL COMMENT '고객 이름' COLLATE 'utf8mb4_general_ci' AFTER `upw`,
        CHANGE COLUMN `regdate` `regdate` TIMESTAMP NULL DEFAULT NULL COMMENT '고객 가입일' AFTER `name`;

        ALTER TABLE `users`
        CHANGE COLUMN `uid` `uid` VARCHAR(32) NOT NULL COMMENT '고객의 로그인 ID' COLLATE 'utf8mb4_general_ci' AFTER `id`,
        CHANGE COLUMN `name` `name` VARCHAR(32) NOT NULL COMMENT '고객 이름' COLLATE 'utf8mb4_general_ci' AFTER `upw`,
        CHANGE COLUMN `regdate` `regdate` TIMESTAMP NOT NULL COMMENT '고객 가입일' AFTER `name`;
    
    6. 회원가입 -> insert
        - insert into users <데이터베이스명>.<테이블명> (컬럼명, 컬럼명, ...) values (컬럼값, 컬럼값, ...);
        - ` : 키워드를 테이블명, 컬럼명 등 사용하면 백틱을 통해 처리가능
        - now : mysql 내장함수로써 현재 시간을 리턴
        - INSERT INTO `ml_db`.`users` (`uid`, `upw`, `name`, `regdate`) VALUES ('guest', '1234', '게스트', now());
    
    7. 회원 정보 수정 -> update
    
    8. 회원 탈퇴 -> delete
        - 1년간 보관? 완전 삭제?
    
    9. 로그인 -> select (쿼리의 분량이 가장 많다)
        -- 회원 가입 여부 조회 -> 로그인 처리 쿼리
        -- 대소문자 구분 안한다
        -- 제시한 아이디와 비번과 일치하는 row 데이터를 가져와서 uid, name, regdate 값을 출력하시오
        SELECT `uid`, `name`, regdate FROM users WHERE `uid` = 'guest' AND `upw` = '1234';
'''

'''
    파이썬에서 DB에 접속, 접속 해제
'''
import pymysql as my

connection = None
try:
# 1. 접속
    connection = my.connect(host        = 'localhost',  # 127.0.0.1, 서버 주소
                            port        = 3306,         # 포트, 디폴트 포트라 생략 가능
                            user        = 'root',       # 사용자 계정, root 계정 외의 계정 사용 권장
                            password    = 'rlalrlal3',  # 비밀번호
                            database    = 'ml_db',      # 접속할 데이터베이스 
                            # cursorclass = my.cursors.DictCursor
                            )
    print('접속 성공')

except Exception as e:
    print('접속 오류', e)

else:
    print('접속시 문제 없음')

finally:
    # 2. 접속 종료(I/O) -> close()
    if connection:
        connection.close()
    print('접속 종료 성공')
