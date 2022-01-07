from aiogram import executor
from dispetcher import dp
from handlers import personal_actions,callbacks
if __name__ == '__main__':
	print('started')
	executor.start_polling(dp,skip_updates = True)