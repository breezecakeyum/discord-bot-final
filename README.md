# 🎲 Discord Dice Roller Bot

A lightweight, D&D-inspired Discord bot for rolling dice, retrieving dice info, and simulating full dice sets. Built with Python and `discord.py`.

---

## ✨ Features

- 🎯 Roll dice with modifiers (e.g. `!roll 4d6+2`)
- 📚 Get descriptions of standard dice types (`!diceinfo d20`)
- 🎲 Roll one of each standard die (`!rollall`)
- ⚠️ Friendly error handling for invalid input

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/discord-dice-bot.git
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```
### 3. Set Up Environment Variables
Create a .env file in the root directory with the following discord bot token:
```bash
API_KEY=your_discord_bot_token_here
```

### 4. Run the Bot
```bash
python bot.py
```

---

## 🧠 Commands

| Command             | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `!roll dX`          | Rolls a single die (e.g., `!roll d20`)                                      |
| `!roll NdX±M`       | Rolls N dice of type X with optional modifier M (e.g., `!roll 3d6+2`)       |
| `!diceinfo dX`      | Displays usage info for a specific die type (e.g., `!diceinfo d12`)         |
| `!rollall`          | Rolls one of each standard die (d4, d6, d8, d10, d12, d20)                  |

---

## 🧩 Code Structure

### `bot.py`
- Loads environment variables from `.env`
- Starts the bot using the API key

### `bot_commands.py`
- Initializes the bot with command prefix `!`
- Defines commands:
  - `!roll`: roll dice with optional modifiers
  - `!diceinfo`: get info about a specific die
  - `!rollall`: roll one of each standard die
- Handles errors and bot readiness

### `bot_functions.py`
- Contains:
  - `dice_info`: dictionary of die descriptions
  - `dice_maximums`: dictionary of die max values
  - `DiceRollResult`: class to format roll results
  - `parse_dice_roll`: parses strings like `4d20+5`
  - `validate_dice_type`: checks if die type is valid
  - `roll_dice`: rolls dice and returns results

---

## 🛡️ Input Validation

- ✅ Supported dice: `d4`, `d6`, `d8`, `d10`, `d12`, `d20`, `d100`
- 🚫 Maximum 100 dice per roll
- ➕ Supports modifiers (e.g., `+5`, `-2`)
- 🧾 Invalid formats return helpful error messages
- ❓ Unknown dice types prompt a list of supported options

---

## 🧪 Example Usage

```text
!roll d20
!roll 4d6+3
!roll 2d10-1
!diceinfo d8
!rollall
