from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os
import random
import shutil
from api_token import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['delete_account'])
async def delete_account_command(message: types.Message):
	path = "data/" + str(message.from_user.username)
	if os.path.isdir(path) == True:
		shutil.rmtree(path)
		await message.reply("Ваш аккаунт удален")
	else:
		await message.reply("Сначала зарегистрируйся!\n/reg")

@dp.message_handler(commands=['rullet'])
async def rullet_command(message: types.Message):
	path = "data/" + str(message.from_user.username)
	if os.path.isdir(path) == True:
		balance = str(path) + "/balance.txt"
		file = open(balance, "r")
		my_money = file.read()
		file.close()
		if int(my_money) > 100:
			rullet = random.randint(1,3)
			if rullet == 1:
				win_money_list = ["50", "100", "150"]
				win_money = random.choice(win_money_list)
				file = open(balance, "tw")
				money = int(my_money) + int(win_money)
				file.write(str(money))
				file.close()
				await message.reply("Поздравляю ты выиграл " + str(win_money))
			else:
				lose_money_list = ["50", "100"]
				lose_money = random.choice(lose_money_list)
				file = open(balance, "tw")
				money = int(my_money) - int(lose_money)
				file.write(str(money))
				file.close()
				await message.reply("Ты проиграл " + str(lose_money))
		else:
			await message.reply("Недостаточно средств.")
	else:
		await message.reply("Сначала зарегистрируйся!\n/reg")

@dp.message_handler(commands=['balance'])
async def balance_command(message: types.Message):
	path = "data/" + str(message.from_user.username)
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
        path = "data/" + str(message.from_user.username)
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

@dp.message_handler(commands=['flip_coin'])
async def flip_coin_command(message: types.Message):
	flip_coin = ["Орёл.", "Решка."]
	coin = random.choice(flip_coin)
	await message.reply(str(coin))

@dp.message_handler(commands=['gay'])
async def gay_command(message: types.Message):
	gay_list = ["10%","20%","30%","40%","50%","60%","70%","80%","90%","100%"]
	gay = random.choice(gay_list)
	await message.reply("Ты гей на " + str(gay))

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
