from aiogram import Bot, Dispatcher
from filters import IsAdminFilter
import config 

bot = Bot(token=config.BOT_TOKEN,parse_mode='Html')
dp = Dispatcher(bot)

dp.filters_factory.bind(IsAdminFilter)
