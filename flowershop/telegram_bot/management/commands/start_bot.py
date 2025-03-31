import asyncio
import os
import logging
from django.core.management.base import BaseCommand
from telegram_bot.bot import bot, dp  # Используем уже созданные объекты

logging.basicConfig(level=logging.INFO)

async def main():
    logging.info("Бот запущен!")
    db_path = "data/db.sqlite3"
    if os.path.exists(db_path):
        logging.info(f"✅ База данных найдена: {db_path}")
    else:
        logging.error("❌ База данных не найдена!")
    await dp.start_polling(bot)

class Command(BaseCommand):
    help = "Запускает Telegram-бота"

    def handle(self, *args, **kwargs):
        asyncio.run(main())  # Запускаем бота