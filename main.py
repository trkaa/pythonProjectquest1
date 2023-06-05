from aiogram import executor
# from handlers import dp, GeoState
from handlers import dp
from loader import db
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apsched import send_message_time
from datetime import datetime


async def on_start(_):
    try:
        db.create_table_check_points()
        print("DB connected...OK!")
        print('бот запущен')


    except:
        print('DB failure')


scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
scheduler.add_job(send_message_time, trigger='date', run_date=datetime(2023, 6, 5, 15, 14), args=(dp,))
scheduler.start()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start)
