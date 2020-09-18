# Reminders for first class
import config
import telebot
import schedule
import time

from multiprocessing.context import Process
from config import id1, admin_id
from text import text_1, text_3
from telebot import types
bot = telebot.TeleBot(config.API_TOKEN)
#
@bot.message_handler(commands=['tuk'])
def start(message):
    bot.send_message(message.chat.id, "Бот запущен")


def start_process():  # Запуск Process


    p1 = Process(target=Reminder.start_schedule, args=()).start()


class Reminder():  # Class для работы с schedule
    def start_schedule():  # Запуск schedule
        # Параметры для schedule
        #schedule.every(42).minutes.do(Reminder.send_message)
        #schedule.every(53).minutes.do(Reminder.send_message1)
        # Напоминание про урок с вечера 20:00
        schedule.every().monday.at("20:00").do(Reminder.send_message)
        schedule.every().thursday.at("20:00").do(Reminder.send_message)
        # Напоминание утром перед уроками
        schedule.every().tuesday.at("06:30").do(Reminder.send_message)
        schedule.every().friday.at("06:30").do(Reminder.send_message)

        while True:  # Запуск цикла
            schedule.run_pending()
            time.sleep(1)

    # Функции для выполнения заданий по времени
    def send_message():
        bot.send_message(id1, text_3)

    def send_message1():
        bot.send_message(id1, text_1)

if __name__ == '__main__':
    start_process()
    try:
        bot.polling(none_stop=True)
    except:
        pass