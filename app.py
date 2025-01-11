
from flask import Flask

app = Flask (__name__)

@app.route ('/')
def Ola_Pessoal():
    return "Ola Pessoal !!"


if __name__ == '__main__':
    app.run (debug=True)

    