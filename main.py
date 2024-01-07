from apscheduler.schedulers.background import BackgroundScheduler
import re

scheduler = BackgroundScheduler()


def reminder_handler(reminder_text):
    print("Напоминание:", reminder_text)


def process_user_input(user_input):
    match = re.match(r'^напомни (.+)$', user_input, re.IGNORECASE)

    if match:
        reminder_text = match.group(1)
        scheduler.add_job(reminder_handler, 'interval', minutes=5, args=[reminder_text], id=reminder_text)
        print(f"Напоминание установлено: {reminder_text}")
    else:
        print("Не удалось распознать команду напоминания.")
    try:
        while True:
            user_input = input("Введите текст: ")
            process_user_input(user_input)
    except KeyboardInterrupt:
        scheduler.shutdown()


if __name__ == "__main__":
    scheduler.start()

