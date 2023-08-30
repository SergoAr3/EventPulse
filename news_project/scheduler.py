import schedule
import time
from pages.utils import save_latestNews_to_database

def run_task():
    try:
        save_latestNews_to_database()
    except Exception as e:
        print(f"Ошибка при выполнении задачи: {e}")

# Запускайте задачу каждые два часа
schedule.every(2).hours.do(run_task)

while True:
    schedule.run_pending()
    time.sleep(1)
