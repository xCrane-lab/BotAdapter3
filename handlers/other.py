from aiogram import Router
from aiogram.types import Message
from Text.Text_Ru import TEXT_RU
from aiogram.filters import Command

router = Router()

# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=TEXT_RU['/help'])

@router.message()
async def send_answer(message: Message):
    await message.answer(text=TEXT_RU['other_answer'])