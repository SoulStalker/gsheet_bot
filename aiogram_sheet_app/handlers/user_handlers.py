import asyncio

from aiogram import F, Router, Bot
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, FSInputFile

from aiogram_sheet_app.services import (
    get_sheet_data,
    get_worksheet_info,
    get_sheet_id,
)

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
        chat_id=message.chat.id,
        text="Список команд:\n"
        "/help - список команд\n/get_sheets - список таблиц\n/get_sheet_info - получить данные из таблицы",
    )


@router.message(Command(commands=["get_sheet_info"]))
async def get_sheet_info(message: Message, bot: Bot, state: FSMContext):
    sheet = await get_sheet_id()
    sheets_list = await get_worksheet_info(sheet)
    await bot.send_message(
        chat_id=message.chat.id,
        text=f"Список таблиц:\n{sheets_list}",
    )


# @router.message(Command(commands=["get_sheet_data"]))
# async def get_data(message: Message, bot: Bot, state: FSMContext):
#     print(data[0]["id"])
#     await bot.send_message(
#         chat_id=message.chat.id,
#         text=data[0]["id"],
#     )
