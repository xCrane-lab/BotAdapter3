from config_reader import config
import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers import start, menu, other, registration

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Для записей с типом Secret* необходимо
# вызывать метод get_secret_value(),
# чтобы получить настоящее содержимое вместо '*******'
bot = Bot(token=config.bot_token.get_secret_value(), parse_mode='HTML')
# Диспетчер
dp = Dispatcher()

# Запуск процесса поллинга новых апдейтов
async def main():
    dp.include_routers(start.router, registration.router, menu.router, other.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())