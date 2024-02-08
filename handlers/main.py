from dispatcher import main_router, bot
from aiogram import F
from aiogram.types import (
    Message,
    CallbackQuery,
    ReactionTypeEmoji,
)
from aiogram.fsm.context import FSMContext
import keyboard_markup
from states import admin
import config


@main_router.message(F.text == "test")
async def test_mes_info(message: Message, state: FSMContext) -> None:
    await message.answer(
        text=f"chat_id: {message.chat.id}, thread_id: {message.message_thread_id}"
    )


@main_router.message(F.text.in_(["Севастополь", "Севас следующая неделя"]))
async def one_of_cities(message: Message, state: FSMContext) -> None:
    city = message.text
    await state.update_data(city=city)
    await message.answer(
        text="Выбери день недели", reply_markup=keyboard_markup.menu_week_sevas()
    )
    await state.set_state(admin.choise_day_of_week)

@main_router.message(admin.choise_day_of_week or admin.choise_type_of_order, F.text == "« Назад")
async def cancel(message: Message, state: FSMContext) -> None:
    keyboard = keyboard_markup.menu_cities()
    await message.answer(text="<<", reply_markup=keyboard)

@main_router.message(
    admin.choise_day_of_week, F.text.in_(["Вторник", "Среда", "Четверг", "Пятница"])
)
async def day_of_week(message: Message, state: FSMContext) -> None:
    weekday = message.text
    await state.update_data(weekday=weekday)
    await message.answer(text="Отправь заказ", reply_markup=keyboard_markup.cancel())
    await state.set_state(admin.enter_order)


@main_router.message(F.text.in_(["Симферополь"]))
async def one_of_cities(message: Message, state: FSMContext) -> None:
    city = message.text
    await state.update_data(city=city)
    await message.answer(
        text="Выбери тип заказа", reply_markup=keyboard_markup.menu_type_simf()
    )
    await state.set_state(admin.choise_type_of_order)


@main_router.message(
    admin.choise_type_of_order, F.text.in_(["Срочные заказы", "Предварительные заказы"])
)
async def type_of_order(message: Message, state: FSMContext) -> None:
    type_ = message.text
    await state.update_data(type=type_)
    await message.answer(text="Отправь заказ", reply_markup=keyboard_markup.cancel())
    await state.set_state(admin.enter_order)


@main_router.message(F.text.in_(["Ялта", "Евпатория"]))
async def one_of_cities(message: Message, state: FSMContext) -> None:
    city = message.text
    await state.update_data(city=city)
    await message.answer(text="Отправь заказ", reply_markup=keyboard_markup.cancel())
    await state.set_state(admin.enter_order)




tr_weekday = {
    "Вторник": "tuesday_chat_id",
    "Среда": "wednesday_chat_id",
    "Четверг": "thursday_chat_id",
    "Пятница": "friday_chat_id",
}

tr_type_order = {
    "Срочные заказы": "quick_order_chat_id",
    "Предварительные заказы": "preorder_chat_id",
}

tr_y_and_e = {
    "Ялта": "yalta_chat_id",
    "Евпатория": "evpatoria_chat_id",
}


@main_router.message(admin.enter_order)
async def enter_order(message: Message, state: FSMContext) -> None:
    text_order = message.text
    data = await state.get_data()
    new_text_order = ""
    if text_order == "« Назад":
        match data["city"]:
            case "Севастополь" | "Севас следующая неделя":
                await state.set_state(admin.choise_day_of_week)
                keyboard = keyboard_markup.menu_week_sevas()
            case "Симферополь":
                await state.set_state(admin.choise_type_of_order)
                keyboard = keyboard_markup.menu_type_simf()
            case "Ялта" | "Евпатория":
                keyboard = keyboard_markup.menu_cities()
        return await message.answer(text="<<", reply_markup=keyboard)
    match data["city"]:
        case "Севастополь":
            day_of_week = tr_weekday[data["weekday"]]
            await bot.send_message(
                chat_id=config.data_chat["chat_id"],
                text=text_order,
                message_thread_id=config.data_chat[day_of_week],
            )
            await message.answer(
                text="Записано!", reply_markup=keyboard_markup.menu_cities()
            )
            await state.clear()
        case "Севас следующая неделя":
            choise = data["city"]
            new_text_order = f"‼️{choise}‼️\n\n{text_order}"
            day_of_week = tr_weekday[data["weekday"]]
            await bot.send_message(
                chat_id=config.data_chat["chat_id"],
                text=new_text_order,
                message_thread_id=config.data_chat[day_of_week],
            )
            await message.answer(
                text="Записано!", reply_markup=keyboard_markup.menu_cities()
            )
            await state.clear()
        case "Симферополь":
            type_of_order = tr_type_order[data["type"]]
            await bot.send_message(
                chat_id=config.data_chat["chat_id"],
                text=text_order,
                message_thread_id=config.data_chat[type_of_order],
            )
            await message.answer(
                text="Записано!", reply_markup=keyboard_markup.menu_cities()
            )
            await state.clear()
        case "Ялта" | "Евпатория":
            city_ = tr_y_and_e[data["city"]]
            await bot.send_message(
                chat_id=config.data_chat["chat_id"],
                text=text_order,
                message_thread_id=config.data_chat[city_],
            )
            await message.answer(
                text="Записано!", reply_markup=keyboard_markup.menu_cities()
            )
            await state.clear()
