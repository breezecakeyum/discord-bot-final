import bot_commands
import os
from dotenv import load_dotenv

# Load environment variables from .env file and store it in our variable
load_dotenv()
api_key = os.getenv('API_KEY')

# Run the bottom passing in the API key
bot_commands.bot.run(os.getenv('API_KEY'))
