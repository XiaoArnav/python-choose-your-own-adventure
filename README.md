# The Lost Kingdom Adventure

A simple command-line choose-your-own-adventure game written in Python. Explore three paths, make decisions, discover different endings, and play again as many times as you like.

This project was created for **Global Hack Week: Hacktoberfest — Use GitHub Copilot to Build a Simple Application**.

## Features

- Three starting paths: a whispering forest, a dragon's cave, and a rushing river
- Multiple choices and endings
- Input validation for invalid menu selections
- End-of-run result tracking (`win` or `survive`) with a final score display
- Replay support
- No external dependencies

## Requirements

- Python 3.8 or newer

## Run the game

Clone the repository, change into its directory, and run:

```bash
python adventure.py
```

On some systems, you may need to use:

```bash
python3 adventure.py
```

## How to play

1. Choose a numbered path when prompted.
2. Read the story and select what your character should do next.
3. After reaching an ending, choose whether to play again.
4. Each run ends with a result summary and score:
   - `You won this adventure!` -> score `2`
   - `You survived this adventure!` -> score `1`

Invalid menu entries are rejected until a valid number is entered.

## Run tests

This project includes lightweight tests using Python's standard library (`unittest`):

```bash
python -m unittest -v
```

## Project structure

```text
.
├── adventure.py
├── LICENSE
└── README.md
```

## Challenge submission

This project is a valid **Global Hack Week: Hacktoberfest** Copilot challenge submission.

It demonstrates using GitHub Copilot to build and improve a beginner-friendly Python CLI application with:
- branching story logic
- input validation
- replay support
- automated tests
- a scoring/result system added after the initial scaffold

Ready-to-use submission text:

> I completed the Global Hack Week: Hacktoberfest "Use GitHub Copilot to complete any coding challenge" task by building and improving **The Lost Kingdom Adventure**, a Python choose-your-own-adventure CLI game. I used GitHub Copilot to develop the game logic, add input validation, implement replay and score tracking (win/survive outcomes), and add unit tests with Python's standard library.  
> Repository: https://github.com/XiaoArnav/python-choose-your-own-adventure

## License

This project is available under the MIT License.
