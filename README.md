# Arch Technologies - Python Development Internship (Month 2)

Month 2 projects for the **Python Development Internship** at **Arch Technologies**.

**Intern:** Salik Hussain
**Domain:** Python Development
**Email:** salikhussain71@gmail.com

---

## Projects

### Task 3 - Number Guessing Game
The computer randomly picks a number between 1 and 100 and the player keeps guessing. After each guess the program gives a hint: too high or too low.

**Features**
- Random secret number (`random.randint(1, 100)`)
- "Too high" / "Too low" hints
- Input validation (letters and out-of-range numbers are rejected)
- Best score tracking and play-again option

**Run:**
```
python Task3_Number_Guessing_Game/number_guessing_game.py
```

### Task 4 - ATM Simulation
A simple ATM system built with Object-Oriented Programming. The `ATM` class holds the account data and banking logic, and the `ATMController` class handles user interaction.

**Features**
- PIN login (3 attempts, then the card is blocked)
- Check balance, deposit, and withdraw
- Mini statement of recent transactions
- Encapsulation with private attributes
- Handles invalid amounts, insufficient funds, and wrong menu options

**Run:**
```
python Task4_ATM_Simulation/atm_simulation.py
```
Demo PIN: `1234` (starting balance: $1,000.00)

---

## Concepts Practiced
- Random numbers, loops, and conditional statements
- Functions and input validation (`try/except`)
- Classes, objects, and encapsulation
- Separation of logic and user interaction

## Requirements
- Python 3.x (tested on Python 3.14)
- No extra packages needed (standard library only)

## Folder Structure
```
Task3_Number_Guessing_Game/   number_guessing_game.py
Task4_ATM_Simulation/         atm_simulation.py
Screenshots/                  screenshots of the working programs
```

## Screenshots
See the `Screenshots` folder for the programs running in Visual Studio Code.

---

*Submitted as part of the Arch Technologies Python Development Internship.*
