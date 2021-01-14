from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    # ===== 모델 가져오기 ===== #
    from . import models
    # 1. DB 변경 적용 (리비전 파일 생성)
    # flask db migrate 실행
    # 2. DB 갱신
    # flask db upgrade

    # 블루프린트
    from .views import main_views, question_views, answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)

    return app
