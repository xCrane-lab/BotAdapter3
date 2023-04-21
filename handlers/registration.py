from aiogram import Router, F, types
from aiogram.types import Message
from Text.Text_Ru import TEXT_RU
from aiogram.filters import Command, StateFilter, Text, CommandObject
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from admins import list_admins
from FSM.States import Registr
from Database.user import con, cur
from bot import bot
from aiogram.utils.keyboard import InlineKeyboardBuilder


router = Router()
user = []


# Этот хэндлер будет срабатывать на команду "/cancel" в любых состояниях,
# кроме состояния по умолчанию, и отключать машину состояний
@router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(text=TEXT_RU['Fcancel'])
    # Сбрасываем состояние
    await state.clear()


# Этот хэндлер будет срабатывать на команду "/cancel" в состоянии
# по умолчанию и сообщать, что эта команда доступна в машине состояний
@router.message(Command(commands='cancel'), StateFilter(default_state))
async def process_cancel_command(message: Message):
    await message.answer(text=TEXT_RU['Scancel'])


@router.message(Command(commands=['registration']), StateFilter(default_state))
async def name(message: Message, state: FSMContext, command: CommandObject):
    user_id = str(message.from_user.id)
    if user_id not in list_admins:
        user.append(message.from_user.id)
        await message.answer(text=TEXT_RU['name'])
        await state.set_state(Registr.fill_name)
    else:
        data = command.args.split(', ')
        userid, fullname, group = data
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="Да",
            callback_data=f'reg_yes_{userid}')
        )
        builder.add(types.InlineKeyboardButton(
            text="Нет",
            callback_data=f'reg_no_{userid}')
        )
        await message.answer(
            f"Нажмите на кнопку, чтобы подтвердить или отказать в регистрации Адаптера:"
            f"\n<b>ФИО:</b> {fullname}"
            f"\n<b>Номер группы:</b> {group}",
            reply_markup=builder.as_markup()
        )

@router.callback_query(lambda c: 'reg' in c.data)
async def sign_up(callback: types.CallbackQuery):
    if 'yes' in callback.data:
        user_id = callback.data.split('_')[2]
        cur.execute('''insert into users values (?);''', [user_id])
        con.commit()
        await bot.send_message(chat_id=user_id, text=TEXT_RU['ConA'])
    elif 'no' in callback.data:
        user_id = callback.data.split('_')[2]
        await bot.send_message(chat_id=user_id, text=['FCon'])


@router.message(StateFilter(Registr.fill_name), F.text)
async def process_name_sent(message: Message, state: FSMContext):
    # Cохраняем введенное имя в хранилище по ключу "name"
    user.append(message.text)
    await message.answer(text=TEXT_RU['Group'])
    await state.set_state(Registr.fill_group)


# Этот хэндлер будет срабатывать, если во время ввода имени
# будет введено что-то некорректное
@router.message(StateFilter(Registr.fill_name))
async def warning_not_name(message: Message):
    await message.answer(text=TEXT_RU['NotAName'])


@router.message(StateFilter(Registr.fill_group), lambda x: x.text.split('/')[0].isdigit() and x.text.split('/')[1].isdigit())
async def process_name_sent(message: Message, state: FSMContext):
    user.append(message.text)
    await message.answer(text=TEXT_RU['MFC'])
    for admin in list_admins:
        await bot.send_message(chat_id=admin, text=f"Пользователь {user[1]} из группы {user[2]} запрашивает регистрацию." \
                                                   f"\nЧтобы подтвердить регистрацию или отказать в ней"
                                                   f"\nПропишите команду /registration {user[0]}, {user[1]}, {user[2]}")
    await state.clear()


# Этот хэндлер будет срабатывать, если во время ввода возраста
# будет введено что-то некорректное
@router.message(StateFilter(Registr.fill_group))
async def warning_not_age(message: Message):
    await message.answer(
        text=TEXT_RU['NotAGroup'])

