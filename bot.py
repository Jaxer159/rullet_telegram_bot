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

@dp.message_handler(commands=['chat_id'])
async def chat_id_command(message: types.Message):
    await message.reply("ID этого чата: \n" + "`" + str(message.chat.id) + "`", parse_mode='MarkdownV2')

@dp.message_handler(commands=['id'])
async def id_command(message: types.Message):
    await message.reply("ID пользователя " + str(message.from_user.first_name) + ":\n" + "`" + str(message.from_user.id) + "`", parse_mode='MarkdownV2')

if __name__ == '__main__':
    executor.start_polling(dp)
