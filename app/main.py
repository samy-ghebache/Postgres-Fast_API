from fastapi import FastAPI, Depends
from db_connection import establish_connection
from routers import router1

# Connect to the database
try:
    cursor = establish_connection()
except:
    print('Error while connecting to the database')
    exit()

app = FastAPI()

app.cursor = cursor 
app.include_router(router1.router)

@app.get("/endpoint1")
async def get_users():
    try:
        app.cursor.execute("""
        select * from student;
        """)
        return cursor.fetchall()
    except:
        return {}



    






    
    