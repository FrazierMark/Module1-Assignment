# Import the flask library for usage.
from flask import Flask
import random

# create an instance of the flask server
app = Flask(__name__)

# Index/base route
@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'


@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'


@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return f'How did you know I liked {users_dessert}?'


@app.route('/madlibs/<adjective>/<noun>')
def madlib(adjective, noun):
    """ Displays random funny story using URL params"""
    return f'I absolutely love to swim in my {adjective} {noun}!'


@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    """ Displays the product of two numbers"""
    if number1.isdigit() and number2.isdigit():
        return f'{number1} times {number2} is {int(number1) * int(number2)}.'
    else:
        return 'Invalid inputs. Please try again by entering 2 numbers!'


@app.route('/sayntimes/<word>/<n>')
def say_n(word, n):
    """Repeats a string a given number of times"""
    if n.isdigit() and int(n) > 0 and word.isalpha():
        return (word + ' ') * int(n)
    else:
        return 'Invalid input. Please try again by entering a word and a number!'


@app.route('/dicegame')
def play_dice():
    """Plays a dice game"""
    dice_roll = random.randint(1, 6)
    if dice_roll > 5:
        return f'You rolled a {dice_roll}. You won!'
    return f'You rolled a {dice_roll}. You lost!'

if __name__ == '__main__':
    app.run(debug=True)