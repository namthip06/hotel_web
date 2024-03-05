from pydantic import BaseModel

class Pay(BaseModel):
    name : str
    hotel : str
    room : str
    check_in : str
    check_out : str
