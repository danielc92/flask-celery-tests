from flask import Flask
from flask_celery_ import make_celery
from flask_sqlalchemy import SQLAlchemy
from random import choice
from string import ascii_lowercase
from datetime import datetime

app = Flask(__name__)

app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:12345@localhost:5432/test',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)


celery = make_celery(app)
db = SQLAlchemy(app)


# Database Schema
class Results(db.Model):
    __tablename__ = 'results'

    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data', db.String(100))

# Drop the table(s) in schema and recreate it
db.drop_all()
db.create_all()

@celery.task(name='inserter')
def insert():
    """Insert large amount of records to cause a delay."""
    for num in range(5000):
        data = ''.join([choice(ascii_lowercase) for i in range(20)])
        result = Results(data=data)
        db.session.add(result)
    db.session.commit()

    return 'Commit Successful.'


@app.route('/process')
def process():

    start = datetime.now()
    insert()
    end = datetime.now() - start

    return '<code style="font-size: 3rem; color: green;">request has been successfully sent. finished in {}</code>'.format(end)

@app.route('/async')
def process_async():

    insert.delay()

    return '<code style="font-size: 3rem; color: green;"><strong>async</strong> request has been successfully sent.</code>'


if __name__ == '__main__':
    app.run(debug=True)