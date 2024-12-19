import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from aiogram_sheet_app.config import load_config
from aiogram_sheet_app.handlers import other_router

storage = MemoryStorage()


async def main():
    config = load_config(".env")
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher(storage=storage)

    dp.include_router(other_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
