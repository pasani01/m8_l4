from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .obj_data import CatagoryData

request_contact = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Telefon raqami", request_contact=True)],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

request_location = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Joylashuvni yuborish", request_location=True)],
    ],
    resize_keyboard=True,
    one_time_keyboard=True

)

category_data = CatagoryData() 
categories = category_data.get_catagory()

select_category = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton(text=item[1], callback_data=f"category:{item[0]}")] for item in categories
    ]
)