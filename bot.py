from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os
from api_token import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['balance'])
async def balance_command(message: types.Message):
	path = "data/balance/" + str(message.from_user.username)
	if os.path.isdir(path) == True:
		balance = str(path) + "/balance.txt"
		file = open(balance, "r")
		my_money = file.read()
		file.close()
		await message.reply("Баланс: " + str(my_money))
	else:
		await message.reply("Сначала зарегистрируйся!\n/reg")

@dp.message_handler(commands=['reg'])
async def reg_command(message: types.Message):
    if str(message.from_user.username) == "None":
        await message.reply("Поставь сначало себе username, а после напиши еще раз \n/reg")
    else:
        path = "data/balance/" + str(message.from_user.username)
        if os.path.isdir(path) == True:
            await message.reply("Ты уже зарегистрировался!")
        else:
            balance = str(path) + "/balance.txt"
            os.mkdir(path)
            file = open(balance, "tw")
            file.write("1000")
            file.close()
            await message.reply("Ты успешно зарегистрировался!")

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