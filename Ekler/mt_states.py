from aiogram.fsm.state import State, StatesGroup

class RegesterStates(StatesGroup):
    waiting_for_first_name = State()  
    waiting_for_last_name = State()  
    waiting_for_phone = State() 
    waiting_for_username = State()  
    waiting_for_location = State()  


class CatagoryStates(StatesGroup):
    waiting_for_category_name = State()  
    waiting_for_category_description = State()

class ObjectStates(StatesGroup):
    waiting_for_object_name = State()  
    waiting_for_object_description = State()  
    waiting_for_object_price = State()  
    waiting_for_object_category = State()  

