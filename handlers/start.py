from aiogram import Router
from aiogram.types import Message, User
from Text.Text_Ru import TEXT_RU
from aiogram.filters import Command
from admins import list_admins
from Database.user import cur
from Text.Text_Ru import TEXT_RU
from handlers import registration



router = Router()

@router.message(Command("start"))
async def start(message: Message):
    user_id = str(message.from_user.id)
    cur.execute("SELECT * FROM users;")
    base = cur.fetchall()
    base = [i[0] for i in base]
    if message.from_user.id not in base:
        await message.answer(text=TEXT_RU['reg'])
    elif user_id not in list_admins:
        await message.answer(TEXT_RU['start'])
    else:
        await message.answer(TEXT_RU['Astart'])
