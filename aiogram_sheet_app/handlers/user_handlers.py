import asyncio

from aiogram import F, Router, Bot
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, FSInputFile

router = Router()


@router.message(CommandStart())
async def start_command(message: Message, bot: Bot, state: FSMContext):
    await bot.send_message(
        chat_id=message.chat.id,
        text="Привет, я бот для взаимодействия с таблицами Google Sheets. Посмотреть команды /help",
    )


@router.message(Command(commands=["help"]))
async def help_command(message: Message, bot: Bot, state: FSMContext):
    await bot.send_message(
        chat_id=message.chat.id, text="Список команд:\n" "/help - список команд\n"
    )
