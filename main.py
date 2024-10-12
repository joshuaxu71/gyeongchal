import os

import hikari
import lightbulb
from dotenv import load_dotenv

from service.config import set_korean_day
from service.message import process_message

# Load environment variables from .env file
load_dotenv()

# Replace 'your-token-here' with your bot's token
BOT_TOKEN = os.getenv("CLIENT_TOKEN")

# Initialize the bot
my_intents = (
   hikari.Intents.GUILDS
   | hikari.Intents.GUILD_MESSAGES
   | hikari.Intents.MESSAGE_CONTENT
)
bot = lightbulb.BotApp(token=BOT_TOKEN, intents=my_intents, default_enabled_guilds=[703077529342443611])

@bot.listen(hikari.StartedEvent)
async def on_started(event):
   print("Bot is online!")

@bot.listen(hikari.GuildMessageCreateEvent)
async def on_message_create(event: hikari.GuildMessageCreateEvent):
   # Make sure the bot doesn't respond to its own messages
   if event.author.is_bot:
      return
   
   if event.content:
      await process_message(event, event.content)

@bot.command()
@lightbulb.command('enable_korean_day', 'Delete new messages that are not in Korean')
@lightbulb.implements(lightbulb.SlashCommand)
async def enable_korean_day_command(ctx: lightbulb.Context) -> None:
   if ctx.member is None or not (ctx.member.permissions & hikari.Permissions.ADMINISTRATOR):
      return await ctx.respond("This command can only be executed by admins")
    
   await set_korean_day(ctx.guild_id, True)
   await ctx.respond(f'Korean day has been enabled')

@bot.command()
@lightbulb.command('disable_korean_day', 'Allow new messages that are not in Korean')
@lightbulb.implements(lightbulb.SlashCommand)
async def disable_korean_day_command(ctx: lightbulb.Context) -> None:
   if ctx.member is None or not (ctx.member.permissions & hikari.Permissions.ADMINISTRATOR):
      return await ctx.respond("This command can only be executed by admins")
    
   await set_korean_day(ctx.guild_id, False)
   await ctx.respond(f'Korean day has been disabled')

if __name__ == '__main__':
   bot.run()