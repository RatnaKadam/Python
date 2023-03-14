import random
from flask import Flask

# Flask application is created
app = Flask(__name__)


# create a base route address
@app.route('/')
def display_number():
    return f"<h1><b>Guess the Number<b></h1>" \
           "<img src='https://media1.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif?cid=ecf05e47rusbieou7m7omsakd8mf3tlh8ed2eh3jqixvssau&rid=giphy.gif&ct=g'>"


guess = random.randint(0, 9)


@app.route('/<int:number>')
def guess_the_number(number):
    if guess == number:
        return "<h1>Correct!!!</h1>" \
               "<p><img src= 'https://media1.giphy.com/media/12CcmGavTHjSOk/giphy.gif?cid=ecf05e47wz9qmon2qr15j347j6hm8nadot3wzgfs923l7uzp&rid=giphy.gif&ct=g'></p>"
    elif guess < number:
        return "<h1><b>Too High!!</h1></b>" \
               "<p><img src= 'https://media1.giphy.com/media/cQn4uEVVBCAiIdsNoS/giphy.gif?cid=ecf05e47dgfiv4miof0yy5y9gis4qo8k7hpfca32s3mo2nam&rid=giphy.gif&ct=g'></p>"
    else:
        return "<h1><b>Too Low!!</b></h1>" \
               "<p><img src= 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'></p>"


if __name__ == "__main__":
    app.run()
