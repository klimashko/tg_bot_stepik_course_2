from aiogram import Bot, Dispatcher
from aiogram.filters import BaseFilter
from aiogram.types import Message
from environs import Env

env = Env()  # Создаем экземпляр класса Env
env.read_env()  # Методом read_env() читаем файл .env и загружаем из него переменные в окружение

BOT_TOKEN = env('BOT_TOKEN')  # Получаем и сохраняем значение переменной окружения в переменную BOT_TOKEN
# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Список с ID администраторов бота. !!!Замените на ваш!!!
admin_ids: list[int] = [env.int('ADMIN_ID')] # Получаем и сохраняем значение переменной окружения в переменную ADMIN_ID


# Собственный фильтр, проверяющий юзера на админа
class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int]) -> None:
        # В качестве параметра фильтр принимает список с целыми числами
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids


# Этот хэндлер будет срабатывать, если апдейт от админа
@dp.message(IsAdmin(admin_ids))
async def answer_if_admins_update(message: Message):
    await message.answer(text='Вы админ')


# Этот хэндлер будет срабатывать, если апдейт не от админа
@dp.message()
async def answer_if_not_admins_update(message: Message):
    await message.answer(text='Вы не админ')
    
    #Это чтобы узанть свой id и включить его в список admin_ids: list[int] = []
    print(message.from_user.id)


if __name__ == '__main__':
    dp.run_polling(bot)