'''
    메인 서비스를 구축하는 컨트롤러
    - 라우트 : URL과 이를 처리할 함수 연계
    - 비즈니스 로직 : 사용자가 요청하는 주 내용을 처리하는 곳
'''

from flask import render_template, request
# 엔트리포인트가 step2_app_factory이므로 그 아래의 service.controller의 __init__.py에서 bp_main을 들고온다
from service.controllers import bp_main as main

# 127.0.0.1/main/
@main.route('/')
def home():
    return 'main home'