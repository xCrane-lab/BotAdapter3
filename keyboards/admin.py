from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from Text.Text_Ru import TEXT_RU

def admin_menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=TEXT_RU['CHW'])
    kb.button(text=TEXT_RU['DMan'])
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
