from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from api_token import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['ping'])
async def ping_command(message: types.Message):
    await message.reply("Я работаю!")

@dp.message_handler(commands=['start'])
async def ping_command(message: types.Message):
    await message.reply("Привет!. Чтобы посмотреть что я умею \n/help")



if __name__ == '__main__':
    executor.start_polling(dp)
