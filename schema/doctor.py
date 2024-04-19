from pydantic import BaseModel

class Doctors(BaseModel):
     id: int
     name: str
     specialization: str
     phone: str
     is_available: bool = True

class DoctorsCreateEdit(BaseModel):
     name: str
     specialization: str
     phone: str
     is_available: bool = True

doctors: dict[int, Doctors] = {
     0: Doctors(
          id=0, name='doctor 0', specialization='surgery', phone='0800', is_available=True
     ),
     1: Doctors(
          id=1, name='doctor 1', specialization='gynaecology', phone='0801', is_available=True
     ),
     2: Doctors(
          id=2, name='doctor 2', specialization='general', phone='0802', is_available=True
     )
}