from pydantic import BaseModel
from typing import Optional

from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, field) -> ObjectId:
        """
        Valida que el valor `v` sea un ObjectId válido.
        El parámetro `field` es requerido por Pydantic V2, aunque no lo usemos.
        """
        if not ObjectId.is_valid(v):
            raise ValueError("ID de ObjectId inválido")
        return ObjectId(v) 

    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema):
        field_schema.update(type="string")
    

class ScanRequest(BaseModel):
    image_base64: str
    type: Optional[str] = "png"
