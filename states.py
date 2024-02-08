from aiogram.fsm.state import State, StatesGroup

class admin(StatesGroup):
    choise_day_of_week = State()
    choise_type_of_order = State()
    enter_order = State()
