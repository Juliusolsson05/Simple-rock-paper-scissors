# Rock Paper Scissors with ASCII Art - CLI Game

This simple and engaging CLI (Command Line Interface) game allows users to play the classic "Rock, Paper, Scissors" against the computer, enhanced with colorful ASCII art for an elevated gaming experience. Created as a school project, this Python game is not only fun to play but also serves as a great example of implementing user interaction, randomness, and external libraries in a Python script.

## Features

- **Interactive Gameplay**: Players make choices through the command line.
- **ASCII Art Integration**: Leverages the `art` library to display ASCII art for countdown numbers and smiley faces based on the game result.
- **Colorful Output**: Utilizes `colorama` for colorful console output, enhancing user experience.
- **Randomness**: The computer's choices are randomized to ensure a fair game every time.
- **Replayability**: After each game, players are prompted to play again, allowing for continuous play without restarting the script.

## Prerequisites

Before you start playing the game, make sure you have Python installed on your system. Additionally, you'll need the following Python packages:

- `colorama`
- `art`

You can install them using `pip`:

```bash
pip install colorama art
```

## How to Play

1. Run the game script in your terminal or command prompt.
2. The game will prompt you to make a choice:
   - Enter `1` for Rock.
   - Enter `2` for Scissors.
   - Enter `3` for Paper.
3. After your choice, a countdown will begin, and the computer's choice will be displayed.
4. The game will then display the result with a corresponding ASCII art smiley face.
5. You will be prompted to play again. Enter `ja` to continue or `nej` to exit the game.

## Game Rules

- Rock crushes Scissors.
- Scissors cut Paper.
- Paper covers Rock.

If both you and the computer make the same choice, it's a tie.

## Running the Game

To start the game, navigate to the directory containing the script and run:

```bash
python rock_paper_scissors.py
```

Enjoy the game and may the odds be in your favor!

# TODO
 1. **Make it look like a game**: Use the pygame library to make it look a like a game, set the backgroudn to lightgreen with a start button and fancy animations 
