import logging
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
import config
from aiogram import Router


logging.basicConfig(level=logging.INFO)

# prerequisites
if not config.TOKEN:
    exit("No token provided")


# init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(storage=MemoryStorage())
main_router = Router()
dp.include_router(main_router)
