from aiogram.fsm.state import State, StatesGroup

class RegesterStates(StatesGroup):
    waiting_for_first_name = State()  
    waiting_for_last_name = State()  
    waiting_for_phone = State() 
    waiting_for_username = State()  
    waiting_for_location = State()  