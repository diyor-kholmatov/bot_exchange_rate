from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton



#-------MenuOnRu-------
reply_ru_bnt1 = KeyboardButton('💲 Курсы валют')

markup2 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
markup2.add(reply_ru_bnt1)

