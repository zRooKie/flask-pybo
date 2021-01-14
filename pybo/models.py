from pybo import db

# ============= 질문 model 생성 =========================== #


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

# ============= 답변 model 생성 =========================== #


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey(
        'question.id', ondelete='CASCADE'))
    # question = db.relationship('Question', backref=db.backref('answer_set'))
    # 질문 삭제 시 연관된 답변 데이터 모두 삭제 : cascade='all, delete-orphan'
    question = db.relationship('Question', backref=db.backref(
        'answer_set', cascade='all, delete-orphan'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

    # ondelete='CASCADE' : 질문을 삭제하면 해당 질문의 답변도 삭제
    # question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))

    # 답변 Model 에서 질문 Model 을 참조하기 위함.
    # 답변 Model 객체에서 질문 Model 객체의 제목을 참조하려면 answer.question.subject
    # 이렇게 하려면 속성을 추가할 때 db.Column 이 아니라 db.relationship 을 사용해야 한다.
    # question = db.relationship('Question', backref=db.backref('answer_set'))
    # backref : 역참조, question_a 라는 질문 객체에 question_a.answer_set 으로 질문에 달린 답변들을 참조할 수 있다.
