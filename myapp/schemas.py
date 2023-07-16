from random import choices
from ninja import Schema

class ProOut(Schema):
    id : int 
    name : str
    price : float
    #auth : AuOut = None

class customerOut(Schema):
    id : int
    name: str

class orderIn(Schema):
    customer: int
    product: int
    quantity: int
    details: str = None
    
class orderOut(Schema):
    id: int
    customer: customerOut
    product: ProOut
    quantity: int
    
class cartSchema(Schema):
    product: ProOut
    quantity: int 
    

class MassageOut(Schema):
    detail: str



#class AuthOut(Schema):
    #name : str
    #email : str = None
    #phone : str = None



class ProductIn(Schema):
    name : str
    price : float
    image : str 
    is_active : bool 
    is_DrawTool : bool 
    is_rare : bool 
    # language : int = 'AB' 
    # category : str = 'Art' 
    #auth_id : int = None


class ProductOut(ProductIn):
    id : int
    name : str
    price : float
    image : str = None
    is_active : bool
    is_DrawTool : bool
    is_rare : bool
    #auth : AuthOut = None

#class AuOut(Schema):
    #id : int
    #name: str
    #email : str = None
    #phone :str 


