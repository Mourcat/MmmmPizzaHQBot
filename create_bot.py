from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os

from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()


bot = Bot(token='2125360952:AAGK98quCuKWWk0v86bOw38vDSLeoM8vklY')
dp = Dispatcher(bot, storage=storage)