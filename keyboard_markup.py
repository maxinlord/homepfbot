from aiogram.utils.keyboard import ReplyKeyboardBuilder



def menu_week_sevas():
    builder = ReplyKeyboardBuilder()
    builder.button(text='Вторник')
    builder.button(text='Среда')
    builder.button(text='Четверг')
    builder.button(text='Пятница')
    builder.button(text="« Назад")
    builder.adjust(1)
    return builder.as_markup(
        resize_keyboard=True
    )

def menu_type_simf():
    builder = ReplyKeyboardBuilder()
    builder.button(text='Срочные заказы')
    builder.button(text='Предварительные заказы')
    builder.button(text="« Назад")
    builder.adjust(1)
    return builder.as_markup(
        resize_keyboard=True
    )

def menu_cities():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Севастополь")
    builder.button(text="Севас следующая неделя")
    builder.button(text="Симферополь")
    builder.button(text="Ялта")
    builder.button(text="Евпатория")
    builder.adjust(2, 1, 2)
    return builder.as_markup(
        resize_keyboard=True
    )

def cancel():
    builder = ReplyKeyboardBuilder()
    builder.button(text="« Назад")
    builder.adjust(1)
    return builder.as_markup(
        resize_keyboard=True
    )