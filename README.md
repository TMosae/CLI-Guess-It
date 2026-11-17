# GuessIt CLI 🎯

A resilient, interactive command-line number guessing game built in Python. Players attempt to uncover a randomly selected integer between **1 and 500**, guided by dynamic proximity feedback and protected by defensive input validation.

---

## ✨ Key Features

- **Dynamic Proximity Hints:** Uses absolute difference calculations (`abs()`) to evaluate how close each guess is to the target number, providing four distinct levels of feedback (`too low`, `low`, `high`, and `too high`).
- **Crash-Proof Input Validation:** Protects the game loop against non-numeric strings (`ValueError`) and enforces strict boundary checks (`1–500`), preventing crashes and prompting users cleanly on invalid entries.
- **Attempt Counter:** Tracks every valid guess throughout the session and displays the total number of attempts upon victory.
- **Zero External Dependencies:** Built entirely with Python's standard library (`random`), making it lightweight and immediately runnable in any terminal environment.

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Standard Library Modules:** `random` (`random.choice`)

---

## 🚀 Getting Started

### Prerequisites
Ensure you have **Python 3** installed on your system. You can verify this by running:
```bash
python3 --version
```

### Installation & Usage
1. **Clone the repository:**
   ```bash
   git clone https://github.com
   ```
2. **Navigate into the project directory:**
   ```bash
   cd YOUR-REPO-NAME
   ```
3. **Launch the game:**
   ```bash
   python3 GuessIt.py
   ```

---

## 🎮 Example Gameplay

```text
Guess the number: hello
Invalid input, please enter a whole number between 1 and 500
Guess the number: -5
Your guess must be between 1 and 500 please
Guess the number: 250
incorrect! your guess is too high
Guess the number: 112
incorrect! your guess is low
Guess the number: 118
correct! you have guessed the correct number
it took you 3 tries to get it right
```

---

## 🧠 Technical Concepts Demonstrated

- **Control Flow & State Management:** Structuring a continuous `while True` game loop utilizing `continue` to bypass invalid turns and `break` to terminate cleanly upon meeting the win condition.
- **Exception Handling:** Implementing `try / except ValueError` blocks to safely handle type-casting errors from raw `input()` strings.
- **Boolean & Relational Logic:** Combining directional comparisons (`<`, `>`) with distance thresholds (`>= 10`, `< 10`) using logical `and` / `or` operators.

---

## 🔮 Planned Improvements (v2.0)

- **Difficulty Modes:** Add selectable difficulty tiers (e.g., Easy: `1–100`, Medium: `1–500`, Hard: `1–1000`) with adjusted proximity thresholds.
- **Replay Loop & High Scores:** Allow players to start a new round without restarting the script and persist best scores locally using JSON or file I/O.
