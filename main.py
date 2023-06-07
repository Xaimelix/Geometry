from flask import Flask

app = Flask(__name__)
from config import SECRET_KEY
app.config['SECRET_KEY'] = SECRET_KEY


def main():
    app.run()


if __name__ == '__main__':
    main()