from aiogram import types 
from dispetcher import bot,dp
import config 

@dp.callback_query_handler()
async def process_callback_get_link_button(call: types.CallbackQuery):
	# await bot.send_message(message.chat.id,'Post added!',reply_markup=ReplyKeyboardRemove())
	member = await bot.get_chat_member(config.CHANNEL_ID,call.from_user.id)
	if member.status != 'left':
		await bot.answer_callback_query(call.id, show_alert=True, text=call.data)
	else:
		await bot.answer_callback_query(call.id, show_alert=True, text='Подпишитесь на канал и нажмите на кнопку ещё раз!')
