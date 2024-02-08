from dispatcher import main_router
from aiogram import F
from aiogram.types import (
    Message,
)
from aiogram.fsm.context import FSMContext
import keyboard_markup

@main_router.message()
async def test_mes_info(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(text='не понимаю тебя(', reply_markup=keyboard_markup.menu_cities())