from fastapi import APIRouter
from app.models import ScanRequest 
from fastapi import Response, status
from app.baml_client.async_client import b
from baml_py import Image
from typing import List, Any, Dict


router = APIRouter()

@router.post("/tray/", status_code=status.HTTP_200_OK)
async def get_tray(user_request: ScanRequest , response: Response) -> Dict[Any, Any]:
    """
    Endpoint para obtener información de una bandeja específica por su ID.
    """

    try:

        baml_response: List[str] = await b.GetTrayProducts(
            tray=Image.from_base64(
                media_type= f"image/{user_request.type}",
                base64= user_request.image_base64)
                )

        return {
                "success": True,
                "message": "OK",
                "data": baml_response,
                "status_code": status.HTTP_201_CREATED
        } 
    except Exception as e:
        return {
                "success": False,
                "message": str(e),
                "data": str(e), 
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR
        }