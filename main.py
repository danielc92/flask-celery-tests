from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from random import choice
from string import ascii_lowercase


app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqb://localhost//'
app.config['CELERY_BACKEND'] = 'postgresql://postgres:12345@localhost:5432/test'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5432/test'

db = SQLAlchemy(app)


# Database Schema
class Results(db.Model):
    __tablename__ = 'results'

    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data', db.String(100))

db.create_all()


def insert():

    for num in range(1000):
        data = ''.join(choice(ascii_lowercase)) for i in range(20)
        result = Results(data=data)
        db.session.add(result)

    db.session.commit()
    return 'Commit Successful.'


@app.route('/process')
def process():

    return '<code>async request has been successfully sent.</code>'

if __name__ == '__main__':
    app.run(debug=True)