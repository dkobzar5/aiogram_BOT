from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove,InlineKeyboardMarkup,InlineKeyboardButton
from aiogram import types
from dispetcher import dp,bot
import config
import emoji
film_name = 'Unnamed'
photo = None
video = None
caption = None

def makeDefaultMarkup():
	markup = ReplyKeyboardMarkup(resize_keyboard = True)
	btn1 = KeyboardButton('/getfilmname')
	btn2 = KeyboardButton('/setfilmname')
	btn3 = KeyboardButton('/setdescription')
	btn4 = KeyboardButton('/setphoto')
	btn5 = KeyboardButton('/setvideo')
	btn6 = KeyboardButton('/post')
	markup.add(btn1,btn2,btn3,btn4,btn5,btn6)
	return markup
def createFilmButton():
	global film_name
	markup = InlineKeyboardMarkup()
	getname_button = InlineKeyboardButton(text='Название фильма тут', callback_data = film_name)
	markup.add(getname_button)
	return markup
	
@dp.message_handler(lambda message: str(message.from_user.id) in config.BOT_OWNER,commands=['start'])
async def start(message):
	await bot.send_message(message.chat.id,'Bot started', reply_markup = makeDefaultMarkup())

@dp.message_handler(lambda message: str(message.from_user.id) in config.BOT_OWNER,commands=['confirm'])
async def setFilmName(message:types.Message):
	global film_name,photo,caption,video
	media = types.MediaGroup()
	media.attach_photo(photo)
	media.attach_video(video)
	await bot.send_media_group(config.CHANNEL_ID,media=media)
	await bot.send_message(config.CHANNEL_ID,caption,reply_markup=createFilmButton())

	await bot.send_message(message.chat.id,'Post added!',reply_markup=ReplyKeyboardRemove())
	await message.answer('________________________________')
	film_name,photo,caption,video='Unnamed',None,None,None


@dp.message_handler(lambda message: str(message.from_user.id) in config.BOT_OWNER,commands=['reset'])
async def setFilmName(message:types.Message):
	global film_name,photo,caption,video
	film_name,photo,caption,video='Unnamed',None,None,None
	await bot.send_message(message.chat.id,'Post reseted!',reply_markup=makeDefaultMarkup())


@dp.message_handler(lambda message: str(message.from_user.id) in config.BOT_OWNER,commands=['setfilmname'])
async def setFilmName(message:types.Message):
	global film_name
	config.IS_POSTING_FILMNAME = True
	await message.answer('Set film name')


@dp.message_handler(lambda message: str(message.from_user.id) in config.BOT_OWNER,commands=['getfilmname'])
async def getFilmName(message: types.Message):
	global film_name
	await message.answer('Current filmname is "{}"'.format(film_name))

@dp.message_handler(lambda message: str(message.from_user.id) in config.BOT_OWNER,commands=['setphoto'])
async def setPhoto(message: types.Message):
	config.IS_POSTING_PHOTO = True
	await message.answer('Set film photo')

@dp.message_handler(lambda message: str(message.from_user.id) in config.BOT_OWNER,commands=['setvideo'])
async def setVideo(message: types.Message):
	config.IS_POSTING_VIDEO = True
	await message.answer('Set film video')

@dp.message_handler(lambda message: str(message.from_user.id) in config.BOT_OWNER,commands=['setdescription'])
async def setVideo(message: types.Message):
	config.IS_POSTING_DESCRIPTION = True
	await message.answer('Set film description')

@dp.message_handler(lambda message: str(message.from_user.id) in config.BOT_OWNER,commands=['post'])
async def getFilmName(message: types.Message):
		media = types.MediaGroup()
		media.attach_photo(photo)
		media.attach_video(video)
		await bot.send_media_group(message.chat.id,media=media)
		await bot.send_message(message.chat.id,caption,reply_markup=createFilmButton())
		markup = ReplyKeyboardMarkup(resize_keyboard = True)
		confirm_button = KeyboardButton('/confirm')
		reset_button = KeyboardButton('/reset')
		markup.add(confirm_button,reset_button)
		await bot.send_message(message.chat.id,'Confirm if i should post it', reply_markup = markup)



@dp.message_handler(lambda message: str(message.from_user.id) in config.BOT_OWNER,content_types=['text'])
async def handle(message: types.Message):
	if config.IS_POSTING_DESCRIPTION:
		global caption
		config.IS_POSTING_DESCRIPTION = False
		caption = message.text
		await bot.send_message(message.chat.id,emoji.emojize(':thumbs_up:'))
	if config.IS_POSTING_FILMNAME:
		global film_name
		config.IS_POSTING_FILMNAME = False
		film_name = message.text
		await bot.send_message(message.chat.id,emoji.emojize(':thumbs_up:'))

@dp.message_handler(lambda message: str(message.from_user.id) in config.BOT_OWNER,content_types=['photo'])
async def handle(message: types.Message):
	if config.IS_POSTING_PHOTO:
		global photo
		config.IS_POSTING_PHOTO = False
		photo = message.photo[0].file_id
		await bot.send_message(message.chat.id,emoji.emojize(':thumbs_up:'))

@dp.message_handler(lambda message: str(message.from_user.id) in config.BOT_OWNER,content_types=['video'])
async def handle(message: types.Message):
	if config.IS_POSTING_VIDEO:
		global video
		config.IS_POSTING_VIDEO = False
		video = message.video.file_id
		await bot.send_message(message.chat.id,emoji.emojize(':thumbs_up:'))