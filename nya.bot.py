
from aiogram import Bot, Dispatcher
from aiogram.filters import  CommandStart, Text
from aiogram.types import FSInputFile, Message
from random import *

from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

bot: Bot=Bot(token='6119338121:AAE1Sa9HMIvvOeGzMb7TNCGvV0DBGgihRkA')
dp: Dispatcher=Dispatcher()


button3: KeyboardButton=KeyboardButton(text='NYA')
button4: KeyboardButton=KeyboardButton(text='NYAaaaaaa')
keyboard2: ReplyKeyboardMarkup=ReplyKeyboardMarkup(keyboard=[[button3],[button4]])

@dp.message(CommandStart())
async def start_command(message:Message):
    await message.answer(text='Добро пожаловать в НЯ бот!',reply_markup=keyboard2)

@dp.message(Text(text='NYA'))
async def button3_pressed(message:Message):
    await message.answer(text='NAAAAAAAAA')

@dp.message(Text(text='NYAaaaaaa'))
async def button4_pressed(message: Message):
    photo_number=randint(1,6)
    photo = FSInputFile(f'{photo_number}.gif')

    await bot.send_video(chat_id=message.chat.id, video=photo)




if __name__=='__main__':
    dp.run_polling(bot)