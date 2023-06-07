from flask import Flask

from data import db_session

app = Flask(__name__)
from config import SECRET_KEY
app.config['SECRET_KEY'] = SECRET_KEY


def main():
    db_session.global_init("db/geometry.db")
    app.run()


if __name__ == '__main__':
    main()