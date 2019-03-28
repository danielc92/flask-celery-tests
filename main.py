from flask import Flask
from flask_celery_ import make_celery
from flask_sqlalchemy import SQLAlchemy
from random import choice
from string import ascii_lowercase
from datetime import datetime

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5432/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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

@celery.task(name='main.insert')
def insert():

    for num in range(50000):
        data = ''.join([choice(ascii_lowercase) for i in range(20)])
        result = Results(data=data)
        db.session.add(result)

    db.session.commit()


    return 'Commit Successful.'


@app.route('/process')
def process():

    start = datetime.now()
    insert.delay()
    end = datetime.now() - start

    return '<code style="font-size: 3rem; color: green;">request has been successfully sent. finished in {}</code>'.format(end)

if __name__ == '__main__':
    app.run(debug=True)