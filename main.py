import asyncio
from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State


import keyboards as kb
from config import token
from aiohttp import ClientSession

storage = MemoryStorage()
bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)



@dp.message_handler(commands=['start'])
async def process_command_start(message):
    await bot.send_message(message.chat.id, "Hi this is a bot exchange rate \n\n"
                                            "Data source:\n"
                                            "https://nbu.uz/exchange-rates/", reply_markup=kb.markup2)


#-------exchange rate------------
@dp.message_handler()
async def process_command_exchange(message: types.Message):
    await bot.send_sticker(chat_id=message.from_user.id,
                           sticker=r"CAACAgUAAxkBAAEE9zFipFMnGfjEe0SgH3BoxUJScSiE4AACeAADr_PENec4qLjqiXybJAQ")

    if message.text == '💲 Курсы валют' or message.text == '💲 Currency rates' or message.text == '💲 Valyuta kurslari':
        async with ClientSession() as session:
            r = await session.get("https://nbu.uz/exchange-rates/json/")
            json = list(filter(lambda x: x['code'] == "USD", await r.json()))
            json1 = list(filter(lambda x: x['code'] == "CNY", await r.json()))

            value = json[0]['cb_price']
            value1 = json1[0]['cb_price']

            await bot.send_message(message.chat.id, f'$ 1 = {value} UZS\n'
                                                    f'¥ 1 = {value1} UZS\n'
                                                    f'$ 1 = {value1} ¥ 1')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    executor.start_polling(dp)