from dispatcher import main_router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, CommandObject
from aiogram.types import (
    Message,
)
import keyboard_markup



@main_router.message(CommandStart())
async def command_start(
    message: Message, state: FSMContext, command: CommandObject
) -> None:
    await state.clear()
    await message.answer(text='Привет 👋🏻', reply_markup=keyboard_markup.menu_cities())