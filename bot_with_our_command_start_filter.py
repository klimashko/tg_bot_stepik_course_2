from aiogram import Bot, Dispatcher
from aiogram.types import Message
import os
import dotenv


dotenv.load_dotenv() #принимает в качестве аргумента путь к файлу .env
# (если файл лежит в той же директории, что и исполняемый python-скрипт, то можно путь не указывать)
# и загружает переменные из этого файла в окружение, откуда мы их получаем через os.getenv('<имя_пер.-ой>')


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def my_start_filter(message: Message) -> bool:
    return message.text == '/start'


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(my_start_filter)
async def process_start_command(message: Message):
    await message.answer(text='Это команда /start')


if __name__ == '__main__':
    dp.run_polling(bot)