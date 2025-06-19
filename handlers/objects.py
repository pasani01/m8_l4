from aiogram import Router
from aiogram.types import Message,CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import F

from Ekler.obj_data import  ObjectData
from Ekler.mt_states import ObjectStates
from Ekler.keybord import select_category

object_router = Router()

@object_router.message(ObjectStates.waiting_for_object_name)
async def add_object_name_handler(message: Message, state: FSMContext ):
    try:
        object_name = message.text.strip()
        await state.update_data(name=object_name)
        await state.set_state(ObjectStates.waiting_for_object_description)
        await message.answer("objenin aciklamasini girin:")
    except Exception as e:
        await message.answer("Bir hata oluştu!")
        print(e)
        await state.clear()

@object_router.message(ObjectStates.waiting_for_object_description )
async def add_object_description_handler(message: Message, state: FSMContext):
    try:
        description = message.text
        await state.update_data(description=description)
        await state.set_state(ObjectStates.waiting_for_object_price)
        await message.answer("onject fiyatini girin:")
    except Exception as e:
        await message.answer("Bir hata oluştu!")
        print(e)
        await state.clear()


@object_router.message(ObjectStates.waiting_for_object_price )
async def add_object_price_handler(message: Message, state: FSMContext):
    try:
        price=message.text
        await state.update_data(price=price)
        await state.set_state(ObjectStates.waiting_for_object_category)
        await message.answer("lutfen bir katakory secin",reply_markup=select_category)
    except Exception as e:
        await message.answer('bir hata olsutu !')
        print(e)
        await state.clear()

@object_router.callback_query(ObjectStates.waiting_for_object_category, F.data.startswith("category:"))
async def add_object_catagory_handler(callback: CallbackQuery, state: FSMContext):
    try:
        category_id = int(callback.data.split(":")[1])
        await state.update_data(category_id=category_id)
        await callback.message.edit_reply_markup()
        
        data = await state.get_data()

        needed_keys = ["name", "description", "price", "category_id"]
        columns = ", ".join(needed_keys)
        placeholders = ", ".join(["?"] * len(needed_keys))
        values = [data[key] for key in needed_keys]

        object_data = ObjectData()
        object_data.add_object(columns, placeholders, values)

        await callback.answer("Obje eklendi!")
        await state.clear()
    except Exception as e:
        await callback.message.answer("Bir hata oluştu!")
        print(f"Error: {e}")
        await state.clear()
