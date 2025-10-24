
# 📘 Assignment: Games in Python

## 🎯 Objetivo

Build two classic text-based games to practice Python fundamentals: input handling, loops, conditionals, state management, and basic problem decomposition.

## 📝 Tarefas

### 🛠️ Hangman Game

#### Description
Implement the classic word-guessing game. The program randomly selects a hidden word and the player guesses one letter at a time until they either reveal the full word or run out of attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list (at least 8 varied words)
- Display current progress using underscores for unknown letters (e.g. `_ p p l e`)
- Accept a single-letter guess (case-insensitive) each turn
- Track and display remaining incorrect attempts
- Prevent duplicate guesses from consuming an attempt (show a friendly message)
- Track and display letters already guessed
- Detect win (all letters revealed) and loss (attempts exhausted) conditions
- Show a final message with the word revealed

Example (user input shown after >):

```
Word: _ _ _ _ _    Attempts left: 6
Guessed letters:  (none)
> a
Word: a _ _ a _    Attempts left: 6
Guessed letters: a
> z
Word: a _ _ a _    Attempts left: 5
Guessed letters: a, z
...
```

### 🛠️ Number Guessing Game

#### Description
Create a number guessing game where the computer chooses a random integer in a range and the player tries to guess it in as few attempts as possible.

#### Requirements
Completed program should:

- Prompt for difficulty (e.g. easy: 1–20, medium: 1–50, hard: 1–100)
- Randomly choose a number in the selected range
- Repeatedly ask for a guess until correct
- Validate input (must be an integer in range) and reprompt on invalid entries
- Provide feedback: "Too high", "Too low", or "Correct!" each turn
- Track number of attempts and display it when the player wins
- Optionally offer replay at the end (Y/N)

Example:
```
Select difficulty (easy/medium/hard): medium
I'm thinking of a number between 1 and 50.
> 25
Too low.
> 40
Too high.
> 33
Correct! You got it in 3 attempts.
Play again? (y/n): n
```

---

Feel free to extend either game with optional enhancements (color output, hints, score tracking) after meeting core requirements.
