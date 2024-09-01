# Mind Reader Game

This is a game in which a computer tries to predict a player's move. A player has to click on either the Heads or Tails button. The computer will try to predict whether the player will either click on the Heads button or Tails button. If the computer predicts the player's move correctly, then it gets a point else the player gets a point. The game runs till either the player or the computer reaches a score of 50 points.

The game logic implements Claude Shannon's Mind-Reading machine algorithm (https://this1that1whatever.com/miscellany/mind-reader/Shannon-Mind-Reading.pdf).

### Dependencies
The following tools are used to create this game:

1. HTML 5
2. CSS
3. Python
4. Flask
5. JavaScript

### How to Run
Go to the `mind-reader-flask` directory

    `cd mind-reader-flask`

Create a new environment variable

    `python -m venv game-venv`

- Activate the virtual environment

    `source game-venv/bin/activate`

Install the dependencies

    `pip3 install -r requirements.txt`

Run the game

    `python3 app.py`
