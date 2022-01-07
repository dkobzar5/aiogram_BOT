from aiogram import types 
from aiogram.dispatcher.filters import BoundFilter
import config

class IsAdminFilter(BoundFilter):
	"""docstring for ClassName"""
	key = 'is_owner'
	def __init__(self, key):
		self.is_owner = is_owner
	async def check(self, message: types.Message):
		return message.from_user_id==config.BOT_OWNER
		