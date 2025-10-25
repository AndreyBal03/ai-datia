from fastapi import APIRouter
from app.models import ScanRequest 
from fastapi import Response, status
from app.baml_client.async_client import b
from baml_py import Image
from typing import Any, Dict
from bson import ObjectId
from datetime import datetime

router = APIRouter()

@router.post("/tray/{tray}/product/{product_name}", status_code=status.HTTP_200_OK)
async def get_tray(tray: str, product_name: str, user_request: ScanRequest , response: Response) -> Dict[Any, Any]:
    """
    Endpoint para obtener información de la expiration day por una imagen.
    """
    try:
        tray_id = ObjectId(tray)
    except Exception as e:
        return {
            "success": False,
            "message": "Invalid tray ID",
            "data": str(e), 
            "status_code": status.HTTP_400_BAD_REQUEST
        }
    

    try:

        baml_response: str = await b.GetProductExp(
            product=Image.from_base64(
                media_type= f"image/{user_request.type}",
                base64= user_request.image_base64)
                )
        
        uni_date = datetime.fromisoformat(baml_response).timestamp()

        return {
                "success": True,
                "message": "OK",
                "data": uni_date,
                "status_code": status.HTTP_201_CREATED
        } 
    except Exception as e:
        return {
                "success": False,
                "message": str(e),
                "data": [],
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR
        }