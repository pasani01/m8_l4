from aiogram import Bot, Dispatcher 
from aiogram.client.default import DefaultBotProperties

from config import *
from handlers.my_start import start_roter
from handlers.regester import regester_router
from handlers.katagory import catagory_roter
from handlers.objects import object_router
from Ekler.custom_commands import my_commands


async def main():
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(
            parse_mode="HTML",
        )
    )
    await bot.set_my_commands(my_commands)
    dp = Dispatcher()

    dp.include_routers(
        catagory_roter,
        object_router,
        regester_router,
        start_roter,
    )
    await dp.start_polling(bot)

if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    import asyncio
    asyncio.run(main())