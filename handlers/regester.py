from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import F

from Ekler.user_data import UserData
from Ekler.mt_states import RegesterStates
from Ekler.keybord import request_contact, request_location


regester_router = Router()

@regester_router.message(RegesterStates.waiting_for_first_name)
async def first_name_handler(message: Message, state: FSMContext):
    
    try:
        await state.update_data(first_name=message.text)
        await state.set_state(RegesterStates.waiting_for_last_name)
        await message.answer("Lütfen soyadınızı girin:")
    except Exception as e:
        await message.answer("Bir hata oluştu!")
        await state.clear()

@regester_router.message(RegesterStates.waiting_for_last_name)
async def last_name_handler(message: Message, state: FSMContext):
    
    try:
        await state.update_data(last_name=message.text)
        await state.set_state(RegesterStates.waiting_for_phone)
        await message.answer("Lütfen telefon numaranızı girin:",reply_markup=request_contact)
    except Exception as e:
        await message.answer("Bir hata oluştu!")
        await state.clear()


@regester_router.message(RegesterStates.waiting_for_phone, F.contact)
async def phone_handler(message: Message, state: FSMContext):
    try:
        contaxt = message.contact
        await state.update_data(phhone=contaxt.phone_number)
        await state.set_state(RegesterStates.waiting_for_location)
        await message.answer("Lütfen konumunuzu paylaşın:", reply_markup=request_location)
    except Exception as e:
        await message.answer("Bir hata oluştu!")
        await state.clear()


@regester_router.message(RegesterStates.waiting_for_phone)
async def phone_handler_eror(message: Message, state: FSMContext):
    await message.answer("Lütfen telefon numaranızı gönderin.", reply_markup=request_contact)

@regester_router.message(RegesterStates.waiting_for_location, F.location)
async def location_handler(message: Message, state: FSMContext):
    try:
        location = message.location
        location_str = f"{location.latitude}, {location.longitude}"
        await state.update_data(location=location_str)
        await state.update_data(username=message.from_user.username)
        user_data = await state.get_data()
        data = UserData()
        data.create_user(user_data, str(message.from_user.id))

        location = message.location
        await state.update_data(location=location)

        updated_data = await state.get_data()

        await message.answer(
            f"Merhaba {updated_data.get('first_name')} {updated_data.get('last_name')},\n"
            f"aramıza hoş geldiniz!"
        )
        await state.clear()
    except Exception as e:
        await message.answer("Bir hata oluştu!")
        print(f"Error: {e}")
        await state.clear()


@regester_router.message(RegesterStates.waiting_for_location)
async def location_handler_error(message: Message, state: FSMContext):
    await message.answer("Lütfen konumunuzu paylaşın.", reply_markup=None)
    await state.set_state(RegesterStates.waiting_for_location)