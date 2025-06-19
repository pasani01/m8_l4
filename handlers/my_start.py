from aiogram import Router
from aiogram.filters import CommandStart,Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from Ekler.user_data import UserData
from Ekler.mt_states import RegesterStates

start_roter = Router()

@start_roter.message(CommandStart())
async def start_handler(message: Message,state:FSMContext):
    user_data = UserData()
    user_id = str(message.from_user.id)

    if not user_data.has_joined(user_id):
        await message.answer('Benim botuma hos geldiniz!')
        user_data.add_user(user_id)
    else:
        await message.answer('geri dondogunuz incin tesekur ederiz !')


@start_roter.message(Command("regester"))
async def regester_handler(message: Message, state: FSMContext):
    try:
        user_data = UserData()
        if not user_data.has_user(str(message.from_user.id)):
            await message.answer("Siz siz zatem bizim uyemiz siniz !")
            return
        await state.clear()
        await state.set_state(RegesterStates.waiting_for_first_name)
        await message.answer(f"regester basladi \nAdınızı daxil edin:")
    except Exception as e:
        await message.answer(f"Bir hata oluştu !")
        print(e)
        await state.clear()