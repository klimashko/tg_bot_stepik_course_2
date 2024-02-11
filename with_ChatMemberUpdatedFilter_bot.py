from aiogram import Bot, Dispatcher
from aiogram.filters import Command, ChatMemberUpdatedFilter, KICKED
from aiogram.types import Message, ChatMemberUpdated
from environs import Env

env = Env()  # Создаем экземпляр класса Env
env.read_env()  # Методом read_env() читаем файл .env и загружаем из него переменные в окружение

BOT_TOKEN = env('BOT_TOKEN')  # Получаем и сохраняем значение переменной окружения в переменную BOT_TOKEN
# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на блокировку бота пользователем
@dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
async def process_user_blocked_bot(event: ChatMemberUpdated):
    print(f'Пользователь {event.from_user.id} заблокировал бота - сообщение в терминале only')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)



if __name__ == '__main__':
    dp.run_polling(bot)