from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client

#@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приветствую! Проголодались?', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Напишите боту в ЛС,\nhttp://t.me/MmmmPizzaHQBot')
        
async def pizza_workout(message: types.Message):
    await bot.send_message(message.from_user.id, 'ВС-ЧТ с 9.00 до 20.00, ПТ-СБ с 10.00 до 23.00')

async def pizza_place(message: types.Message):
    await bot.send_message(message.from_user.id, 'г. Кириши, проспект Героев, 23')
        
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_workout, commands=['режим_работы'])
    dp.register_message_handler(pizza_place, commands=['где_находится'])