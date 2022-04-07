from aiogram import types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

from config import bot, dp


@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Hello {message.from_user.first_name}")


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply("Hi")


@dp.message_handler(commands=['quiz'])
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


@dp.callback_query_handler(lambda call: call.data == "button_call_1")
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


@dp.callback_query_handler(lambda call: call.data == "button_call_2")
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


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
