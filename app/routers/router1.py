from fastapi import APIRouter
from fastapi import Request

router = APIRouter()

@router.get("/endpoint1")
async def get_users(request: Request):
        request.app.cursor.execute("""
        select * from student;
        """)
        return request.app.cursor.fetchall()
