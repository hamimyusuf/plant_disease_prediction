from fastapi import APIRouter, Body, File, UploadFile, Form
from fastapi.encoders import jsonable_encoder
import fileinput

router = APIRouter()

@router.post("/",response_description="post image file")
async def uploadImage(image : UploadFile = File(...)):
    return{
        None
    }