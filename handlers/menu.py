from aiogram import Router
from aiogram.types import Message, User
from Text.Text_Ru import TEXT_RU
from aiogram.filters import Command
from admins import list_admins
from keyboards.user import user_menu
from keyboards.admin import admin_menu
from Database.user import cur



router = Router()

# Этот хэндлер срабатывает на команду /menu
@router.message(Command(commands=['menu']))
async def menu(message: Message):
    user_id = str(message.from_user.id)
    cur.execute("SELECT * FROM users;")
    base = cur.fetchall()
    base = [i[0] for i in base]
    if message.from_user.id not in base:
        await message.answer(text=TEXT_RU['reg'])
    elif user_id not in list_admins:
        await message.answer(TEXT_RU['menu'], reply_markup=user_menu())
    else:
        await message.answer(TEXT_RU['Amenu'], reply_markup=admin_menu())
