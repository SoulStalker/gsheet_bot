from aiogram import Router
from aiogram.types import Message, CallbackQuery

router = Router()


@router.message()
async def send_message(message: Message):
    await message.answer(text=message.text)


@router.callback_query()
async def callback_query(callback: CallbackQuery):
    text = callback.data
    await callback.message.answer(f"{text}")
