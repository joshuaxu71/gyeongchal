from model.config import Config, config_collection

config_cache = {}

async def set_korean_day(guild_id: int, is_korean_day: bool):
   config_cache.pop(guild_id, None)
   return config_collection.update_one(
      {'guildId': guild_id},
      {'$set': {f'isKoreanDay': is_korean_day}},
      upsert=True
   )
   
def is_korean_day(guild_id: int):
   config = __get_config_by_guild_id(guild_id)
   if config:
      return config.isKoreanDay
   return False
   
def __get_config_by_guild_id(guild_id: int):
   config = None
   if guild_id in config_cache:
      config = config_cache[guild_id]
   else:
      config = config_collection.find_one({"guildId": guild_id})
      config_cache[guild_id] = config
   
   if config:
      return Config(**config)
   return None