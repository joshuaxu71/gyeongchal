from typing import Optional

from pydantic import BaseModel, Field
from pymongo import ASCENDING

from data.mongo import db


class Config(BaseModel):
   guildId: int
   isKoreanDay: bool = Field(default=False)

config_collection = db['config']

index_names = config_collection.index_information()
if 'guild_id_index' not in index_names:
   config_collection.create_index([("guildId", ASCENDING)], name="guild_id_index", background=True)