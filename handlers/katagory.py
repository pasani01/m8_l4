from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import F

from Ekler.obj_data import CatagoryData
from Ekler.mt_states import CatagoryStates

catagory_roter = Router()

@catagory_roter.message(CatagoryStates.waiting_for_category_name)
async def add_category_name_handler(message: Message, state: FSMContext):
    try:
        category_name = message.text.strip()
        print(category_name)
        if not category_name:
            await message.answer("Kategoriya adı boş ola bilməz!")
            return
        await state.update_data(name=category_name)
        await state.set_state(CatagoryStates.waiting_for_category_description)
        await message.answer("katagori eklendi. \nsimdi aciklama yazın:")
        
    except Exception as e:
        await message.answer("Bir hata oluştu!")
        print(e)
        await state.clear()

@catagory_roter.message(CatagoryStates.waiting_for_category_description)
async def add_category_description_handler(message: Message, state: FSMContext):
    try:
        category_description = message.text.strip()

        if not category_description:
            await message.answer("Kategoriya açıklaması boş ola bilməz!")
            return
        await state.update_data(description=category_description)
        data = await state.get_data()
        category_data = CatagoryData()
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?"] * len(data))
        values = list(data.values())
        category_data.add_category(columns, placeholders, values)
        await message.answer("Kategoriya başarıyla eklendi!")
        await state.clear()
    except Exception as e:
        await message.answer("Bir hata oluştu!")
        print(e)
        await state.clear()

