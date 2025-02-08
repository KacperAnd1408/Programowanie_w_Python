from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def guess_text():
    return ("<b><h1>Guess a number between 0 and 9</h1></b>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>")

rand_number = random.randint(0, 9)


@app.route("/<int:number>")
def game(number):
    if number == rand_number:
        return ("<h1 style=color: green><b>You found me!</b></h1>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>")
    elif number > rand_number:
        return ("<h1 style=color: purple><b>Too high, try again!</b></h1>"
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>")
    else:
        return ("<h1 style=color: red><b>Too low, try again!</b></h1>"
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>")




if __name__ == "__main__":
    app.run(debug=True)