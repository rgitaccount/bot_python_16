from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards import client_kb
from config import bot


async def hello(message: types.Message):
    await bot.send_message(message.chat.id,
                           f"Hello {message.from_user.first_name}",
                           reply_markup=client_kb.start_markup)


async def help(message: types.Message):
    await message.reply("1. /quiz command will start quiz series of problems\n"
                        "Whenever you press Следующая Викторина will appear next quiz\n"
                        "Note: Bot-Admin will delete cursed words, so that's why be careful")


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Следующая Викторина",
                                         callback_data="button_call_1")
    markup.add(button_call_1)
    question = "How old is Putin"
    answers = [
        "50+", "60+", "70+", "80+", "Immortal"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        explanation="This is a joke",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(hello, commands=['start'])
    dp.register_message_handler(help, commands=['help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
