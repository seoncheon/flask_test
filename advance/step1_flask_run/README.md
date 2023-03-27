# 어플리케이션 구동
    - flask 명령상 기본으로 찾는 파일 -> 아래 파일들은 공존하면 의도치 않은 것이 수행될 수 있다
        - 아래 파일들 중 하나만 필요(각자 우선순위가 존재하기 때문에 의도와는 다르게 실행도리 수 있다)
        - wsgi.py
        - app.py
        - 환경변수에 지정된 파일을( ex: FLASK_APP = xxx )찾는다
    - 커스텀 설정
        1. 환경변수를 지정하고 실행 -> OS에 설정하거나 혹은 shell(맥/리눅스) or cmd(윈도우) 작성해서 구동
            - set FLASK_APP=start_app
            - flask run
        2. 환경변수 파일을 읽어서 처리
            - conda install python-dotenv -y
            - pip install python-dotenv
            - 파일 생성
                - env.config
                - start_app.py
            - 실행
                - flask -e ./env.config run
        3. 명령 수행시 옵션 제공
            - flask --app start_app run --debug run

# 실습
    - wsgi.py 파일 생성
    - 현재 디렉토리로 이동 후 flask run을 실행하면 app.run() 없이 실행
    ```
    * Debug mode: off
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
    127.0.0.1 - - [27/Mar/2023 10:24:22] "GET / HTTP/1.1" 200 -
    ```