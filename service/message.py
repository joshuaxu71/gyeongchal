import re

import hikari
from pymongo import DESCENDING

from service.config import is_korean_day


async def process_message(event: hikari.GuildMessageCreateEvent, message: str):
   if is_korean_day(event.guild_id):
      message_language_input = __check_message_language_input(message)
      if message_language_input == None or message_language_input == 'EN':
         await event.message.delete()
         await event.get_channel().send(f'한국어만 말씀해 주세용~')

# def __valid_language_inputs(event: hikari.GuildMessageCreateEvent):
#    guild = event.get_guild()
#    member = guild.get_member(event.author.id)

#    valid_language_inputs = set()
#    if member:
#       language_input = get_language_input(event.guild_id)
   
#       roles = member.get_roles()
#       for role in roles:
#          if language_input.get(str(role.id), None):
#             valid_language_inputs.add(language_input[str(role.id)])
         
#    return valid_language_inputs

def __check_message_language_input(message: str):
   korean_pattern = re.compile(r'[\u3131-\u318E\uAC00-\uD7A3]')
   english_pattern = re.compile(r'[a-zA-Z]')

   korean = bool(korean_pattern.search(message))
   english = bool(english_pattern.search(message))

   if korean and not english:
      return "KR"
   elif english and not korean:
      return "EN"