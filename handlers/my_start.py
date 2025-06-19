from aiogram import Router
from aiogram.filters import CommandStart,Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from Ekler.user_data import UserData
from Ekler.obj_data import CatagoryData, ObjectData
from Ekler.mt_states import RegesterStates, CatagoryStates, ObjectStates

start_roter = Router()

@start_roter.message(CommandStart())
async def start_handler(message: Message,state:FSMContext):
    user_data = UserData()
    user_id = str(message.from_user.id)

    if user_data.has_joined(user_id):
        await message.answer('Benim botuma hos geldiniz!')
        user_data.add_user(user_id)
    else:
        await message.answer('geri dondogunuz incin tesekur ederiz !')


@start_roter.message(Command("regester"))
async def regester_handler(message: Message, state: FSMContext):
    try:
        user_data = UserData()
        print(user_data.has_user(str(message.from_user.id)))
        if user_data.has_user(str(message.from_user.id)):
            await message.answer("Siz siz zatem bizim uyemiz siniz !")
        else:
            await state.clear()
            await state.set_state(RegesterStates.waiting_for_first_name)
            await message.answer(f"regester basladi \nAdınızı daxil edin:")
    except Exception as e:
        await message.answer(f"Bir hata oluştu !")
        print(e)
        await state.clear()



@start_roter.message(Command("addcatagory"))
async def add_category_handler(message: Message, state: FSMContext):
    try:
        user_data = UserData()
        if user_data.has_user(str(message.from_user.id)):
            await state.clear()
            await state.set_state(CatagoryStates.waiting_for_category_name)
            await message.answer(f"Kategoriya əlavə etmək üçün adınızı daxil edin:")
        else:
            await message.answer("Öncə regester olun!")
    except Exception as e:
        await message.answer(f"Bir hata oluştu !")
        print(e)
        await state.clear()

@start_roter.message(Command("listcategory"))
async def list_category_handler(message: Message):
    try:
        category_data = CatagoryData()
        data= category_data.get_catagory()
        categories = [item[1] for item in data]
        await message.answer("Kategori listesi:\n" + "\n".join(categories))
    except Exception as e:
        await message.answer(f"Bir hata oluştu !")
        print(e)

@start_roter.message(Command("addobject"))
async def add_object_handler(message: Message, state: FSMContext):
    try:
        user_data = UserData()
        if user_data.has_user(str(message.from_user.id)):
            await state.clear()
            await state.set_state(ObjectStates.waiting_for_object_name)
            await message.answer(f"objecin adini giriniz :")
        else:
            await message.answer("Öncə regester olun!")
    except Exception as e:
        await message.answer(f"Bir hata oluştu !")
        print(e)
        await state.clear()