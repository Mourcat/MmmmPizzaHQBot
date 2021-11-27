from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btn_load = KeyboardButton('/загрузить')
btn_delete = KeyboardButton('/удалить')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).row(btn_load, btn_delete)