from datetime import datetime
import time
import sqlite3
import discord
import bot_functions
import re
import random

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!",intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready!")

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"⚠️ Error: {str(error)}")

@bot.command(name="diceinfo")
async def dice_info_command(ctx, die: str):
    die = die.lower()
    if die in bot_functions.dice_info:
        await ctx.send(bot_functions.dice_info[die])
    else:
        await ctx.send("```❓ Unknown die type. Please use one of: d4, d6, d8, d10, d12, d20, d100.```")

@bot.command(name="roll")
async def dice_roll_command(ctx, roll):
    """
    Roll dice with optional modifiers.
    Examples: !roll 4d20+5, !roll d6, !roll 2d10-3, !roll 4d12
    """
    try:
        # Parse the roll string
        parsed = bot_functions.parse_dice_roll(roll)
        if not parsed:
            await ctx.send("```❓ Invalid dice format. Use format like: 4d20+5, d6, or 2d10-3```")
            return

        dice_count, die_type, modifier = parsed

        # Validate dice type
        if not bot_functions.validate_dice_type(die_type):
            valid_dice = ", ".join(sorted(bot_functions.dice_maximums.keys()))
            await ctx.send(f"```❓ Unknown die type. Please use one of: {valid_dice}.```")
            return

        # Validate reasonable limits
        if dice_count > 100:  # Prevent spam/abuse
            await ctx.send("```❓ Maximum 100 dice per roll.```")
            return

        if dice_count < 1:
            await ctx.send("```❓ Must roll at least 1 die.```")
            return

        # Roll the dice
        rolls = bot_functions.roll_dice(dice_count, die_type)

        # Create result and send message
        result = bot_functions.DiceRollResult(dice_count, die_type, rolls, modifier)
        await ctx.send(result.format_message(ctx.author))

    except ValueError as e:
        await ctx.send("```❓ Invalid dice format. Use format like: 4d20+5, d6, or 2d10-3```")
    except Exception as e:
        await ctx.send("```❌ An error occurred while rolling dice. Please try again.```")

@bot.command(name="rollall")
async def dice_roll_all_command(ctx):
    #Dictionary to store our die types
    dice_types = [4, 6, 8, 10, 12, 20]

    # Running a for loop through all the available die types
    dice_rolls = {f'd{n}': random.randint(1, bot_functions.dice_maximums[f'd{n}']) for n in dice_types}


    # Formatting the message and running through a for loop to output all the dice rolls
    message_lines = [f'{ctx.author}:']
    for n in dice_types:
        message_lines.append(f'Your d{n} rolled a {dice_rolls[f"d{n}"]}')

    # Final formatting result
    await ctx.send(f'```' + '\r\n'.join(message_lines) + f'```')

class DiscordClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    if message.author == self.user:
      return