from flask import Flask
from flask_sqlalchemy import SQLAlchemy #импортируем заранее установленную алхимию

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False  # адекватное отображение кирилицы в браузере
db = SQLAlchemy(app)