from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


btn1 = KeyboardButton('/режим_работы')
btn2 = KeyboardButton('/где_находится')
btn3 = KeyboardButton('/меню')
btn4 = KeyboardButton('Поделиться номером', request_contact=True)
btn5 = KeyboardButton('отправить где я', request_location=True)
#btn6 =
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.row(btn1, btn2, btn3).row(btn4, btn5)