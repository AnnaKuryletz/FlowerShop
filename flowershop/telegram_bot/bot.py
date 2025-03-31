import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from telegram_bot.bot_tools import handlers
import django
from shop.models import Order

orders = Order.objects.all()
print(orders)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "flowershop.settings")
django.setup()
# Загружаем переменные окружения
load_dotenv()

TOKEN = os.getenv("TOKEN_BOT")
if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN не найден в .env файле!")

# Создаем экземпляры бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Импортируем и регистрируем обработчики (если они есть)
from telegram_bot.bot_tools import handlers

dp.include_router(handlers.router)  # Приветственное сообщение
# dp.include_router(orders.router)  # Заказы