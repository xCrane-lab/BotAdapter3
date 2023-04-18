from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from Text.Text_Ru import TEXT_RU

def user_menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=TEXT_RU['HW'])
    kb.button(text=TEXT_RU['Abs'])
    kb.button(text=TEXT_RU['Man'])
    kb.adjust(3)
    return kb.as_markup(resize_keyboard=True)