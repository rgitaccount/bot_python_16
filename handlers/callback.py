from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode

from config import bot


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("Следующая Викторина",
                                         callback_data="button_call_2")
    markup.add(button_call_2)
    question = "By whom invented Python"
    answers = [
        "Harry Potter",
        "Putin",
        "Voldemort",
        "Griffin",
        "Linus Torvalds",
        "Guido Van Rossum",
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=5,
        explanation="This is a joke",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )


async def quiz_3(call: types.CallbackQuery):
    question = "Results of print:"
    answers = [
        "1",
        "2",
        "3",
        "4",
        "-1"
    ]
    photo = open("media/flex_2.jpg", "rb")
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="This is too easy for explanation",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2,
                                       lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quiz_3,
                                       lambda call: call.data == "button_call_2")
