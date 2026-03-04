from pydantic import BaseModel, EmailStr, constr

class ContactForm(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: constr(pattern=r"^[0-9]{10}$")
    message: constr(min_length=10, max_length=150)