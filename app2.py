
from flask import Flask

app = Flask (__name__)

@app.route ('/users/<int:user_id>')
def get_user(user_id):
    return f"Usuario com Id {user_id}"


if __name__ == '__main__':
    app.run (debug=True)

    