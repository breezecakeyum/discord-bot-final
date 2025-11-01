import random
import re

dice_info = {
    "d4": "```🔺 D4 – Used for light weapon damage (daggers), healing spells like *Cure Wounds*, and some cantrips.```",
    "d6": "```🔹 D6 – Common for weapon damage (shortswords), sneak attacks, and ability score generation.```",
    "d8": "```🔹 D8 – Used for medium weapon damage (longswords), healing, and hit dice for some classes.```",
    "d10": "```🔹 D10 – Used for spell damage (*Eldritch Blast*), heavy weapons, and percentile rolls.```",
    "d12": "```🔹 D12 – Used for high-damage weapons (greataxes), and hit dice for Barbarians.```",
    "d20": "```🔹 D20 – Core mechanic die for attacks, saving throws, skill checks, and initiative.```",
    "d100": "```🔹 D100 – Used for percentile rolls, loot tables, and wild magic surges (rolled as two d10s).```"
}
dice_maximums = {
    "d4": 4,
    "d6": 6,
    "d8": 8,
    "d10": 10,
    "d12": 12,
    "d20": 20,
    "d100": 100
}

class DiceRollResult:
    def __init__(self, dice_count, die_type, rolls, modifier=None):
        self.dice_count = dice_count                            # How many dice are being rolled
        self.die_type = die_type                                # The type of die being used
        self.rolls = rolls                                      # List of die results if multiple die used
        self.roll_total = sum(rolls)                            # Sum of all dice rolls
        self.modifier = modifier                                # Modifier
        self.final_total = self.roll_total + (modifier or 0)    # Total including any modifiers

    def format_message(self, author):
        """Format the dice roll result as a Discord message"""
        dice_desc = f"{self.dice_count} d{self.die_type}" if self.dice_count > 1 else f"d{self.die_type}"

        message_parts = [
            f"{author}:",
            f"Your {dice_desc} rolled a {self.roll_total}"
        ]

        if self.dice_count > 1:
            message_parts.append(f"Die List: {self.rolls}")

        if self.modifier:
            modifier_str = f"+{self.modifier}" if self.modifier > 0 else str(self.modifier)
            message_parts.extend([
                f"You have a modifier of {modifier_str}",
                f"Your combined roll is {self.final_total}"
            ])
        else:
            message_parts.append("You have no modifiers applied")

        return "```" + "\r\n".join(message_parts) + "```"


def parse_dice_roll(roll_string):
    """Parse a dice roll string like '4d20+5' or 'd6-2'"""
    # Match patterns like: 4d20+5, d6, 2d10-3s
    pattern = r'^(\d*)d(\d+)([+-]\d+)?$'
    match = re.match(pattern, roll_string.strip())

    if not match:
        return None

    dice_count_str, die_type_str, modifier_str = match.groups()

    # Default to 1 die if no count specified
    dice_count = int(dice_count_str) if dice_count_str else 1
    die_type = int(die_type_str)

    # Parse modifier if present
    modifier = None
    if modifier_str:
        modifier = int(modifier_str)

    return dice_count, die_type, modifier


def validate_dice_type(die_type):
    """Check if the die type is valid"""
    return f'd{die_type}' in dice_maximums


def roll_dice(dice_count, die_type):
    """Roll the specified number of dice"""
    max_value = dice_maximums[f'd{die_type}']
    return [random.randint(1, max_value) for _ in range(dice_count)]