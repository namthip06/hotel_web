from pydantic import BaseModel

class Pay(BaseModel):
    name : str
    hotel : str
    room : str
    check_in : str
    check_out : str

class Sign_up(BaseModel):
    user_name : str
    user_password : str
    tel_num : str
    email : str
