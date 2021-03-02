from database import AsyncPSQL
import asyncio

db = AsyncPSQL(
    "database", 
    "user", 
    "host", 
    "password"
)

async def foo():
    return await db.fetchval("SELECT something FROM table WHERE object = $1;", "value")

loop = asyncio.get_event_loop()
loop.run_until_complete(create_table())